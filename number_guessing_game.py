'''
Number-guessing game - player has to guess a randomly generated number between 1 and 10 in amount of attempts specified by chosen level of difficulty
1. choose level of difficulty
2. specify if you want or don't want to get a hint about generated number
3. try to guess that number before you'll run out of attempts
'''
import random
# program creates a function which checks if number from the user's input is correct, too low or too high
def guess(x, y):
    if x == y:
        return "Correct answer"
    else:
        if x < y:
            return "Your guess is too low"
        if x > y:
            return "Your guess is too high"

print("Try to guess a randomly generated number between 1 and 10")
# program randomly generates three numbers - number that has to be guessed and two other numbers that wil be used for hints generation
num = random.randint(1,10)
num2 = random.randint(1,3)
num3 = random.randint(1,10)
# program creates a variable which is used to store amount of available attempts
level = 0
# program creates a dictionary which is used to store available levels of difficulty and amount of attempts available in every one of them
level1 = {"very easy":8, "easy":6, "normal":4, "hard":2}
# program takes chosen level of difficulty from the player and gives him certain amount of available attempts based on chosen level of difficulty. If user chooses unavailable level of difficulty, program raises ValueError
print("levels of difficulty:\nvery easy - 8 attempts\neasy - 6 attempts\nnormal - 4 attempts\nhard - 2 attempts")
level2 = str(input("Choose level of difficulty: "))
if level2 != "very easy" and level2 != "easy" and level2 != "normal" and level2 != "hard":
    raise ValueError("player chose incorrect level of difficulty")
else:
    level = level1[level2]
# program asks user if they want to get a hint and gives them a hint if they want it
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
# program creates a loop which iterates through all available attempts, shows accuracy of user's guesses and outputs correct number if user hasn't guessed it before all their attempts ran out
i = 1
while i <= level:
    x = int(input("Attempt number {}: ".format(i)))
    print(guess(x, num))
    if i == level:
        print("You ran out of attempts. Correct answer is {}".format(num))
    i = i+1
    if x == num:
        break