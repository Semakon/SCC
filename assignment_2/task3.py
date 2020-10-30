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

# Calculate Hammaing Distance by XOR'ing v1 and v2
ham = []
for i in range(len(v1)):
    ham.append(task3.eval(pk, XOR, [v1[i], v2[i]]))

print(len(v1))
print(len(v2))
print(len(ham))
