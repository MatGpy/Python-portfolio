'''
tic tac toe game:
1. choose a game mode (sp - single player (player a - you, player b - program) mp - game mode for two players (player a chooses a sign))
2. choose a sign you want to play as (x or o)
3. during your turn, choose a place on the board where you want to place your sign, in a pattern: rc (r - row, c - column)
4. if one of the players puts three of their signs in a row or in a slant, they win
5. if both players put three of their signs in a row or in a slant during the same turn, game ends with a draw
6. if all places on a board get occupated before one of the players wins or before game ends with a draw, game ends with no result
'''
# program asks user which game mode they want to choose and raises ValueError when chosen sign is different from x or o
import random
tryb = str(input("choose a game mode: "))
sa = str(input("choose player's a sign: "))
if sa == "x":
    sb = "o"
if sa == "o":
    sb = "x"
if sa != "x" and sa != "o":
    raise TypeError("something went wrong")
# program creates a table, where signs will be kept
t = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
    ]
i = 0
j = 0
k = 0
while t[0][0] != sa and t[0][1] != sa and t[0][2] != sa or t[0][0] != sb and t[0][1] != sb and t[0][2] != sb or t[1][0] != sa and t[1][1] != sa and t[1][2] != sa or t[1][0] != sb and t[1][1] != sb and t[1][2] != sb or t[2][0] != sa and t[2][1] != sa and t[2][2] != sa or t[2][0] != sb and t[2][1] != sb and t[2][2] != sb or t[0][0] != sa and t[1][1] != sa and t[2][2] != sa or t[0][0] != sb and t[1][1] != sb and t[2][2] != sb or t[0][2] != sa and t[1][1] != sa and t[2][0] != sa or t[0][2] != sb and t[1][1] != sb and t[2][0] != sb or t[0][0] != sa and t[1][0] != sa and t[2][0] != sa or t[0][0] != sb and t[1][0] != sb and t[2][0] != sb or t[0][1] != sa and t[1][1] != sa and t[2][1] != sa or t[0][1] != sb and t[1][1] != sb and t[2][1] != sb or t[0][2] != sa and t[1][2] != sa and t[2][2] != sa or t[0][2] != sb and t[1][2] != sb and t[2][2] != sb:
    a1 = str(input("player a turn: "))
    t[int(a1[0])-1][int(a1[1])-1] = sa
    print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(t[0][0],t[0][1],t[0][2],t[1][0],t[1][1],t[1][2],t[2][0],t[2][1],t[2][2]))
    i = i+1
    if i == 9:
        print("the end")
        break
    if tryb == "sp":
        b1 = random.randint(1,3)
        b2 = random.randint(1,3)
        while t[b1-1][b2-1] == "x" or t[b1-1][b2-1] == "o":
            b1 = random.randint(1,3)
            b2 = random.randint(1,3)
        t[b1-1][b2-1] = sb
        print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(t[0][0],t[0][1],t[0][2],t[1][0],t[1][1],t[1][2],t[2][0],t[2][1],t[2][2]))
    if tryb == "mp":
        b1 = str(input("player b turn: "))
        t[int(b1[0])-1][int(b1[1])-1] = sb
        print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(t[0][0],t[0][1],t[0][2],t[1][0],t[1][1],t[1][2],t[2][0],t[2][1],t[2][2]))
        i = i+1
    if t[0][0] == sa and t[0][1] == sa and t[0][2] == sa or t[1][0] == sa and t[1][1] == sa and t[1][2] == sa or t[2][0] == sa and t[2][1] == sa and t[2][2] == sa or t[0][0] == sa and t[1][1] == sa and t[2][2] == sa or t[0][2] == sa and t[1][1] == sa and t[2][0] == sa or t[0][0] == sa and t[1][0] == sa and t[2][0] == sa or t[0][1] == sa and t[1][1] == sa and t[2][1] == sa or t[0][2] == sa and t[1][2] == sa and t[2][2] == sa:
        j = 1
    if t[0][0] == sb and t[0][1] == sb and t[0][2] == sb or t[1][0] == sb and t[1][1] == sb and t[1][2] == sb or t[2][0] == sb and t[2][1] == sb and t[2][2] == sb or t[0][0] == sb and t[1][1] == sb and t[2][2] == sb or t[0][2] == sb and t[1][1] == sb and t[2][0] == sb or t[0][0] == sb and t[1][0] == sb and t[2][0] == sb or t[0][1] == sb and t[1][1] == sb and t[2][1] == sb or t[0][2] == sb and t[1][2] == sb and t[2][2] == sb:
        k = 1
    if j+k == 1:
        if j == 1:
            print("player a wins")
            break
        if k == 1:
            print("player b wins")
            break
    if j+k == 2:
        print("draw")
        break
    if i > 9:
        print("the end")
        break