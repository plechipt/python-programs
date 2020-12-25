import json

companies = []

with open('companies_symbols.txt', 'r') as f:
    for companie_index, line in enumerate(f, 0):
        for i, char in enumerate(line, 0):
          if char == '|':
            symbol = line[0:i]
            companies.append({'symbol': '%s' % symbol })
            break

print(companies)

with open('companies.json', 'w') as f:
    json.dump(companies, f)
