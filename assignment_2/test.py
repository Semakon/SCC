import json

with open('json_files/swhe-task2.json') as f:
    data = json.load(f)

print(data)

ciphertext = {
    'Ciphertext Vector': [0, 1, 0, 1, 0, 1]
}

data.update(ciphertext)
print(data)
