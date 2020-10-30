import random

from assignment_2.van_dijk import VanDijk


def XOR(cipher):
    cipher_sum = 0
    for c in cipher:
        cipher_sum += c
    return cipher_sum


def AND(cipher):
    cipher_prod = 1
    for c in cipher:
        cipher_prod *= c
    return cipher_prod


def add(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x


def adder(x, y, van_dijk, pk):
    result = []
    for i in range(len(x) - 1, -1, -1):
        # Prepend x[i] XOR y to result list
        result.insert(0, van_dijk.eval(pk, XOR, [x[i], y]))

        # y is the carry, calculated as x[i] AND y
        y = van_dijk.eval(pk, AND, [x[i], y])

    # Always prepend carry y, since we do not know if it's a 1 or a 0
    result.insert(0, y)
    return result


def add_bits(x: list, y: int):
    result = []
    for i in range(len(x) - 1, -1, -1):
        result.insert(0, x[i] ^ y)
        y = x[i] & y
    result.insert(0, y)
    return result


test = VanDijk(100, 1000, 10, 10)
sk, pk = test.key_gen()

plain = [1, 1, 1]
x0 = [0]
for b in plain:
    x0 = add_bits(x0, b)
print(plain)
print(x0)

cipher = []
for p in plain:
    cipher.append(test.enc(pk, p))

x0 = [test.enc(pk, 0)]
for b in cipher:
    x0 = adder(x0, b, test, pk)

res = []
for c in x0:
    res.append(test.dec(sk, c))

print(plain)
print(res)
