# This program checks if number from the input is ab prime number
# program takes a number from user's input
'''
number = int(input("insert a number: "))
# program raises ValueError if number from the input is negative
if number < 0:
   raise ValueError("incorrect data")
# program tworzy funkcje sprawdzajaca, czy dana liczba jest liczba jest liczba pierwsza. Jej dzialanie opiera sie na zaleznosci, ktora zauwazylem - otoz kazda liczba zlozona musi dzielic sie bez reszty przez 2, 3 lub 5 - jesli dana liczba nie dzieli sie przez zadna z nich, to jest ona liczba pierwsza
#  program creates a function which checks if certain number is a 
def check_if_prime(x):
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
       return("your number is a prime number")
    else:
       return("your number isn't a prime number")
# program sprawdza, czy liczba podana przez uzytkownika jest rowna 0,1,2,3, albo 5 - w takich przypadkach funkcja zwrocilaby nieprawidlowe wyniki, dlatego dla tych przypadkow trzeba indywidualnie przypisac dzialanie programu. Po analizie tej liczby program odpowiada, czy jest ona pierwsza, czy zlozona 
if number == 2 or number == 3 or number == 5:
   print("your number is a prime number")
elif number == 1 or number == 0:
   print("your number isn't a prime number")
else:
   print(check_if_prime(number))
   '''

# this code is under construction