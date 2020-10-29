import json
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


# Load json file
with open('json_files/swhe-task2.json') as f:
    data = json.load(f)

# Parse parameters
pub = data['SWHE']['Public Parameters']
eta = int(pub['eta'])
gamma = int(pub['gamma'])
rho = int(pub['rho'])
tau = int(pub['tau'])

pk = [int(i) for i in pub['pk']]
sk = int(data['SWHE']['sk'])

# Parse Ciphertext Collection
ctc = data['Ciphertext Collection']
for sub in ctc:
    for key in sub:
        sub[key] = int(sub[key])

# Instantiate Van Dijk algorithm
task2 = VanDijk(eta, gamma, rho, tau)

