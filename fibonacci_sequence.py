# Generator of Nth element of Fibonacci sequence (N is chosen by the user)
# program creates function that defines Nth element of Fibonacci sequence
def sequence(x):
# program raises ValueError if user's input is negative
    if x < 0:
        raise ValueError("incorrect data")
    elif x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return sequence(x-2) + sequence(x-1)
# program takes N from user's input and outputs Nth element of Fibonacci sequence 
num = int(input("type N to print Nth element of Fibonacci sequence (N is a number of your choice): "))
print(sequence(num))