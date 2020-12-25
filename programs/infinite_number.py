import os

iterate_number = 2**999999

with open('every_number', 'w') as f:
    for i in range(iterate_number):
        f.write(str(i))
        f.write('\n')