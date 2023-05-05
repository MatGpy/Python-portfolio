# Program do gry w papier kamien nozyce. Program dziala tak, ze uzytkownik wybiera swoj ruch, potem program. Nastepnie ruchy gracza i programu sa porownywane i wyswietlany jest wynik
import random
# program pobiera od uzytkownika jego ruch i zwraca blad, jesli jego ruch jest niezgodny z zasadami gry
player1 = str(input("Now it's your turn (you can choose rock, paper, or scissors): "))
if player1 != "rock" and player1 != "paper" and player1 != "scissors":
    raise ValueError("player chose incorrect option")
# program wybiera swoj ruch w oparciu o wartosc losowo wygenerowanej liczby
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
# program tworzy funkcje do porownywania ruchow gracza i programu
def comparison(x, y):
    if x == "rock" and y == "scissors" or x == "paper" and y == "rock" or x == "scissors" and y == "paper":
        return "player 2 won"
    elif x == "rock" and y == "paper" or x == "paper" and y == "scissors" or x == "scissors" and y == "rock":
          return "you won"
    elif x == "rock" and y == "rock" or x == "paper" and y == "paper" or x == "scissors" and y == "scissors":
          return "draw"
    else:
          return "something went wrong"
# program porownuje ruch gracza z ruchem programu za pomoca uprzednio utworzonej funkcji i pokazuje wynik starcia wraz z ruchem programu
print("player 2: {}\n{}".format(player2_choice(player2), comparison(player2_choice(player2), player1)))