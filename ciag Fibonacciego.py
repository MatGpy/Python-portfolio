def ciag(x):
    if x < 0:
        raise TypeError
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1
    else:
        return ciag(x-2) + ciag(x-1)
    
num = int(input("type X to print Xth element of Fibonacci sequence: "))
print(ciag(num))