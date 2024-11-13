import random

def play():
    user = input("enter 'r' for rock, 's' for scissor and 'p' for paper \n")
    possibilities = ['r', 'p','s']
    computer = random.choice(possibilities)

    if user == computer:
        return 'it\'s  tie'
    
    if win(user, computer):
        return 'you win!'
    
    return 'you loose!'

def win(player,opponent):
    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or \
    player == 'p' and opponent == 'r':
        return True

print(play())