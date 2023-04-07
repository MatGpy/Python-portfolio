def palindrom(x):
    y = str(x)
    m = 0
    i = 0
    l = len(y)-1
    while y[i] == y[l-i]:
          m = m+1
          i = i+1
          if i > l:
             break

    if m == len(y):
       print("is a palindrome")
    else:
       print("isnt a palindrome")
       
number = int(input("type a number: \n"))
print(palindrom(number))