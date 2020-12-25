import random

num_cards = list(range(2,15)) #contains all type of cards

def random_choice(): #picks random card from num_cards
    return random.choice(num_cards)

def players_hand():
    return [random_choice(),random_choice()]

def comptures_hand():
    return players_hand()

comptures_hand()

def bust(hand):
    if sum(hand) > 21:
        return print('You have been busted')

def hit(hand):
    hand.append(random_choice())
    return hand


def more_17():
    pass


def get_input():
    return int(input('Place a bet: '))

def money_exceed():
    pass

def print_board():
    print(f'Players hand: {players_hand()}')
    print(f'Compturs hand: {comptures_hand()}')


if __name__ == '__main__':
    #first the players turn
    while True:
        print_board()
        
