'''
Rock-paper-scissors game
1. choose your move
2. wait for a program to randomly choose a move
3. after that, your move and move of the program will be compared and results will be shown in the output
'''
import random
# program takes user's move from the input and raises ValueError if chosen move is against game's rules
player1 = str(input("Now it's your turn (you can choose rock, paper, or scissors): "))
if player1 != "rock" and player1 != "paper" and player1 != "scissors":
    raise ValueError("player chose incorrect option")
# program chooses its move based on a value of randomly generated number
player2 = random.randint(1,3)
def player2_choice(x):
    if x == 1:
        return "rock"
    elif x == 2:
        return "paper"
    elif x == 3:
        return "scissors"
    else:
        return "something went wrong"
# program creates a function which compares user's move and program's move
def comparison(x, y):
    if x == "rock" and y == "scissors" or x == "paper" and y == "rock" or x == "scissors" and y == "paper":
        return "player 2 won"
    elif x == "rock" and y == "paper" or x == "paper" and y == "scissors" or x == "scissors" and y == "rock":
          return "you won"
    elif x == "rock" and y == "rock" or x == "paper" and y == "paper" or x == "scissors" and y == "scissors":
          return "draw"
    else:
          return "something went wrong"
# program compares player's and program's moves and outputs the result of this comparison
print("player 2: {}\n{}".format(player2_choice(player2), comparison(player2_choice(player2), player1)))