# This program checks if certain number/word/sentence is a palindrome
# program creates a function which checks if certain number/word/sentence is a palindrome
def palindrom(x):
    # program removes spaces from analyzed string
    y = x.replace(" ","")
    j = 0
    i = 0
    length = len(y)-1
    # function uses while loop to check if signs on opposite sides of analyzed string are identical
    while y[i] == y[length-i]:
          j = j+1
          i = i+1
          # program ends while loop if value of i is higher than length of analyzed strings
          if i > length:
             break
    # function checks if value of m is equal to the length of analyzed string (value of m was increased by 1 every time when signs on opposite sides of the string were identical - while loop went through all length of analyzed string, so m is only equal to the length of this string if it's a palindrome)
    if j == len(y):
       return "{} is a palindrome".format(x)
    else:
       return "{} isn't a palindrome".format(x)
# program takes a number/word/sentence from the user's input and outputs the answer      
input = str(input("type a number/word/sentence to check if it's a palindrome: \n"))
print(palindrom(input))