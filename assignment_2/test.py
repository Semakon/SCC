from assignment_2.van_dijk import VanDijk


test = VanDijk(8, 12, 10, 10)
sk, pk = test.key_gen()

print("sk", sk)
print("pk", pk)

plaintext = [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
ciphertext = []
for m in plaintext:
    ciphertext.append(test.enc(pk, m))

decrypted = []
for c in ciphertext:
    decrypted.append(test.dec(sk, c))

print(plaintext)
print(ciphertext)
print(decrypted)
