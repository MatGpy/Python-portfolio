#Kalkulator BMI (Body Mass Index)
# program pobiera od uzytkownika mase ciala (w kilogramach) i wzrost (w centymetrach)
weight = float(input("type your weight in kilograms: ")) 
height = float(input("type your height in centimetres: "))
# program zwraca blad jesli podane zostaly dane w liczbach ujemnych
if weight < 0 or height < 0:
  raise ValueError("incorrect data in input")
# program wylicza BMI na podstawie dostarczonych danych
x = height / 100 
bmi = round(weight/(x**2), 2)
# program wypisuje BMI uzytkownika i informacje o tym jak (nie)prawidlowa jest jego waga
print("Your BMI is: {}".format(bmi))
if bmi <= 18:
  print("your weight is too low")
if bmi > 18 and bmi <= 24:
  print("your weight is perfect")
if bmi > 24 and bmi <= 29:
  print("your weight is a bit too high")
if bmi > 29 and bmi <= 35:
  print("your weight is too high")
if bmi > 35:
  print("your weight is way too high")