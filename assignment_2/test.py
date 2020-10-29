import random

from assignment_2.van_dijk import VanDijk


def XOR(*cipher):
    cipher_sum = 0
    for c in cipher:
        cipher_sum += c
    return cipher_sum


def AND(*cipher):
    cipher_prod = 1
    for c in cipher:
        cipher_prod *= c
    return cipher_prod


test = VanDijk(100, 1000, 10, 10)
sk, pk = test.key_gen()

size = 10
c0 = []
c1 = []
for i in range(size):
    c0.append(test.enc(pk, 0))
    c1.append(test.enc(pk, 1))

xor00 = test.eval(pk, XOR, c0[random.randrange(0, size)], c0[random.randrange(0, size)])
xor01 = test.eval(pk, XOR, c0[random.randrange(0, size)], c1[random.randrange(0, size)])
xor10 = test.eval(pk, XOR, c1[random.randrange(0, size)], c0[random.randrange(0, size)])
xor11 = test.eval(pk, XOR, c1[random.randrange(0, size)], c1[random.randrange(0, size)])
print("XOR:")
print(test.dec(sk, xor00))
print(test.dec(sk, xor01))
print(test.dec(sk, xor10))
print(test.dec(sk, xor11))

and00 = test.eval(pk, AND, c0[random.randrange(0, size)], c0[random.randrange(0, size)])
and01 = test.eval(pk, AND, c0[random.randrange(0, size)], c1[random.randrange(0, size)])
and10 = test.eval(pk, AND, c1[random.randrange(0, size)], c0[random.randrange(0, size)])
and11 = test.eval(pk, AND, c1[random.randrange(0, size)], c1[random.randrange(0, size)])
print("\nAND:")
print(test.dec(sk, and00))
print(test.dec(sk, and01))
print(test.dec(sk, and10))
print(test.dec(sk, and11))

