import json
from assignment_2.van_dijk import VanDijk


# Load json file
with open('json_files/swhe-task1.json') as f:
    data = json.load(f)

# Parse parameters
pub = data['SWHE']['Public Parameters']
eta = int(pub['eta'])
gamma = int(pub['gamma'])
rho = int(pub['rho'])
tau = int(pub['tau'])

pk = [int(i) for i in pub['pk']]
sk = int(data['SWHE']['sk'])

plaintext = data['Plaintext Vector']

# Instantiate Van Dijk algorithm
task1 = VanDijk(eta, gamma, rho, tau)

# Encrypt plaintext
ciphertext = []
for m in plaintext:
    ciphertext.append(task1.enc(pk, m))

# Decrypt plaintext and assert correctness
decrypted = []
for i in range(len(ciphertext)):
    assert task1.dec(sk, ciphertext[i]) == plaintext[i]

# Turn ciphertext into dictionary and add it to json data
cipherdict = {
    'Encrypted Vector': ciphertext
}
data.update(cipherdict)

# Write ciphertext to file
with open('json_files/swhe-task1-done.json', 'w') as f:
    json.dump(data, f, indent=2)
