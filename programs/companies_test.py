import json

with open('companies.json', 'r') as f:
    data = json.load(f)

print(data)
