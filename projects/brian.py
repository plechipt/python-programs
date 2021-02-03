import random

def return_random_number():
    return random.randint(1, 2)

with open('brian_je_gay2.txt', 'w') as f:
    for i in range(1, 100000):
        random_number = return_random_number()
        
        if random_number == 1:
            f.write(f'Bryan je gay {i}')
        
        else:
            f.write(f'Brija je gay XDDDDDD {i}')
            
        f.write('\n')