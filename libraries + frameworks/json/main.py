import json

data = json.loads(open('states.json').read())

for state in data['states']:
    print(state['name'])
