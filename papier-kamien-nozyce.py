import random
v1 = str(input("Now it's your turn: "))
v2 = random.randint(1,3)
def aaa(x):
    if x == 1:
        return "rock"
    if x == 2:
        return "paper"
    if x == 3:
        return "scissors"
def bbb(x, y):
    if x == "rock" and y == "scissors" or x == "paper" and y == "rock" or x == "scissors" and y == "paper":
        return "player 2 won"
    if x == "rock" and y == "paper" or x == "paper" and y == "scissors" or x == "scissors" and y == "rock":
        return "you won"
    if x == "rock" and y == "rock" or x == "paper" and y == "paper" or x == "scissors" and y == "scissors":
        return "draw"
print("player 2: {}\n{}".format(aaa(v2), bbb(aaa(v2), v1)))