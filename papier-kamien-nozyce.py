# Program do gry w papier kamien nozyce. Program dziala tak, ze uzytkownik wybiera swoj ruch, potem program. Nastepnie ruchy gracza i programu sa porownywane i wyswietlany jest wynik
import random
# program pobiera od uzytkownika jego ruch i zwraca blad, jesli jego ruch jest niezgodny z zasadami gry
v1 = str(input("Now it's your turn (you can chose rock, paper, or scissors): "))
if v1 != "rock" and v1 != "paper" and v1 != "scissors":
    raise TypeError
# program wybiera swoj ruch w oparciu o wartosc losowo wygenerowanej liczby
v2 = random.randint(1,3)
def aaa(x):
    if x == 1:
        return "rock"
    if x == 2:
        return "paper"
    if x == 3:
        return "scissors"
# program tworzy funkcje do porownywania ruchow gracza i programu
def bbb(x, y):
    if x == "rock" and y == "scissors" or x == "paper" and y == "rock" or x == "scissors" and y == "paper":
        return "player 2 won"
    if x == "rock" and y == "paper" or x == "paper" and y == "scissors" or x == "scissors" and y == "rock":
        return "you won"
    if x == "rock" and y == "rock" or x == "paper" and y == "paper" or x == "scissors" and y == "scissors":
        return "draw"
# program porownuje ruch gracza z ruchem programu za pomoca uprzednio utworzonej funkcji i pokazuje wynik starcia wraz z ruchem programu
print("player 2: {}\n{}".format(aaa(v2), bbb(aaa(v2), v1)))