# Program bedacy gra polegajaca na odgadnieciu wygenerowanego losowo numeru z przedzialu od 1 do 10 w okreslonej liczbie prob
import random
# program tworzy funkcje sprawdzajaca, czy numer podany przez uzytkownika w danej probie jest prawidlowy, za wysoki, lub za niski
def guess(x, y):
    if x == y:
        return "Correct answer"
    else:
        if x < y:
            return "Your guess is too low"
        if x > y:
            return "Your guess is too high"

print("Try to guess a randomly generated number between 1 and 10")
# program generuje losowo trzy numery - zgadywany numer i dwa inne numery uzywane do generowania wskazowek dla gracza
num = random.randint(1,10)
num2 = random.randint(1,3)
num3 = random.randint(1,10)
# program tworzy zmienna przeznaczona do przechowywania ilosci prob dostepnych dla gracza
level = 0
# program tworzy slownik do przechowywania dostepnych poziomow trudnosci i odpowiadajacych im ilosci prob
level1 = {"very easy":8, "easy":6, "normal":4, "hard":2}
# program pyta uzytkownika o poziom trudnosci, z ktorym chce on grac i daje mu konkretna ilosc prob w zaleznosci od wybranego poziomu trudnosci. Jesli uzytkownik poda poziom trudnosci inny niz podane do wyboru, program zwraca blad
print("levels of difficulty:\nvery easy - 8 attempts\neasy - 6 attempts\nnormal - 4 attempts\nhard - 2 attempts")
level2 = str(input("Choose level of difficulty: "))
if level2 != "very easy" and level2 != "easy" and level2 != "normal" and level2 != "hard":
    raise ValueError("player chose incorrect level of difficulty")
else:
    level = level1[level2]
# program pyta sie uzytkownika o to, czy chce on dostac wskazowke i daje mu ja, jesli uzytkownik tego chce
hint = str(input("Do you want to get a hint? "))
if hint == "yes":
    if num2 == 1:
        if num % 2 == 0:
            print("this number is even")
        if num % 2 != 0:
            print("this number is odd")
    if num2 == 2:
        if num < num3:
            print("this number is lower than {}".format(num3))
        if num >= num3:
            print("this number is higher or equal to {}".format(num3))
    if num2 == 3:
        if num**2 < 10:
            print("this number squared is lower than 10")
        if num**2 >= 10:
            print("this number squared is higher or equal to 10")
if hint != "yes" and hint != "no":
    raise ValueError("incorrect value")
# program tworzy petle iterujaca przez wszystkie dostepne dla uzytkownika proby, pokazuje poprawnosc wykonanych przez uzytkownika prob i wyswietla prawidlowy numer jesli uzytkownik go nie zgadl
i = 1
while i <= level:
    x = int(input("Attempt number {}: ".format(i)))
    print(guess(x, num))
    if i == level:
        print("You ran out of attempts. Correct answer is {}".format(num))
    i = i+1
    if x == num:
        break