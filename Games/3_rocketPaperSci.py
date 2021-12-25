


#3 Question             Rocket, Paper, Scissors

import random

def play():
    user = input("what is your choice: 'r' for rock, 'p' for paper, 's' for scissors : \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s is a tie'

    if is_win(user, computer):
        return "You won!"
    
    return f"you: {user} and the computer: {computer}, you  Lose"
  


def is_win(player, opponent):
      # r > s,  s > p,   p > r   => returns true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
   


print( play() )