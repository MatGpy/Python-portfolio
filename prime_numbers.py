# This program checks if number from the input is a prime number
# program takes a number from user's input
from math import sqrt
number = int(input("insert a number: "))
# program raises ValueError if number from the input is negative
if number < 0:
   raise ValueError("incorrect data")
# program creates a function which checks if certain number is a prime number - it checks if this number can be divided by numbers between 2 and square root of this number
def check_if_prime(x):
   for i in range(2, round(sqrt(x)+1)):
       if x%i == 0:
         return(" isn't a prime number")
   return(" is a prime number")
# program checks if numer from user's input is 0 or 1 (these numbers aren't prime numbers) and if it isn't, program uses a function created previously to check if this number is a prime number
if number == 0 or number == 1:
   print("{} isn't a prime number".format(number))
else:
   print("{}{}".format(number, check_if_prime(number)))
