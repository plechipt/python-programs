import random

while True:
    x = input('Enter first character: ')

    with open('message.txt', 'r') as f:
        words_beggining_with_char = []
        for line in f:

            if line[0] == x[-1]:
                words_beggining_with_char.append(line)

        random_word = random.choice(words_beggining_with_char)
        print(random_word)
