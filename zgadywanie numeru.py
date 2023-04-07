import random
print("Try to guess a number between 1 and 10")
num = random.randint(1,10)
num2 = random.randint(1,3)
num3 = random.randint(1,10)
level = 0
#print(num)
print("levels of difficulty:\nvery easy - 8 attempts\neasy - 6 attempts\nnormal - 4 attempts\nhard - 2 attempts")
level2 = str(input("Choose level of difficulty: "))
if level2 == "very easy":
    level = 8
if level2 == "easy":
    level = 6
if level2 == "normal":
    level = 4
if level2 == "hard":
    level = 2
if level2 != "very easy" and level2 != "easy" and level2 != "normal" and level2 != "hard":
    raise TypeError

hint = str(input("Do you want a hint? "))
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
            print("power of this number is lower than 10")
        if num**2 >= 10:
            print("power of this number is higher or equal to 10")
if hint != "yes" and hint != "no":
    raise TypeError

def guess(x, y):
    if x == y:
        return "Correct answer"
    else:
        if x < y:
            return "Your guess is too low"
        if x > y:
            return "Your guess is too high"
i = 1
while i <= level:
    x = int(input("Attempt number {}: ".format(i)))
    print(guess(x, num))
    if i == level:
        print("You ran out of attempts. Correct answer is {}".format(num))
    i = i+1
    if x == num:
        break