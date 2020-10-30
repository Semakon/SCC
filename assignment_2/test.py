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


def add_bits(x: list, y: int):
    result = []
    carry = y
    for i in range(len(x) - 1, -1, -1):
        result.insert(0, x[i] ^ carry)
        carry = x[i] & carry
    result.insert(0, carry)
    return result


test = VanDijk(100, 1000, 10, 10)
sk, pk = test.key_gen()

plain = [1, 0, 1, 0, 1, 0, 1]
cipher = []
for p in plain:
    cipher.append(test.enc(pk, p))

x = [1, 1, 1, 1, 1]
y = 1
print(x)
print(y)
print(add_bits(x, y))
