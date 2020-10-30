import json
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


# Load json file
with open('json_files/swhe-task3_v2.json') as f:
    data = json.load(f)

# Parse parameters
pub = data['SWHE']['Public Parameters']
eta = int(pub['eta'])
gamma = int(pub['gamma'])
rho = int(pub['rho'])
tau = int(pub['tau'])

pk = [int(i) for i in pub['pk']]

# Parse Ciphertext Collection
v1 = [int(i) for i in data['Ciphertext Collection']["Encrypted V1"]]
v2 = [int(i) for i in data['Ciphertext Collection']["Encrypted V2"]]

# Instantiate Van Dijk algorithm
task3 = VanDijk(eta, gamma, rho, tau)

# Calculate Hammaing Distance
# First, XOR v1 and v2
xor = []
for i in range(len(v1)):
    xor.append(task3.eval(pk, XOR, [v1[i], v2[i]]))

# Then, count no. 1's in xor using an adder
hamming = [task3.enc(pk, 0)]
for b in xor:
    hamming = adder(hamming, b, task3, pk)

# The vectors v1 and v2 are of length 10, so the Hamming Distance is at most
# of size 10 as well. That can be encoded with 4 bits, so take only the 4
# least significant bits as answer.
hamming = hamming[-4:]

# Turn Hamming distance into dictionary and add it to json data
hammingdict = {
    "Encrypted Hamming Distance": hamming
}
data.update(hammingdict)

# Write Hamming distance to file
with open('json_files/swhe-task3_v2-done.json', 'w') as f:
    json.dump(data, f, indent=2)
