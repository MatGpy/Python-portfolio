# Program generujacy N-ty element ciagu Fibonacciego (N wybiera uzytkownik)
# funkcja okreslajaca wartosc N-tego elementu ciagu Fibonacciego
def sequence(x):
    if x < 0:
        raise TypeError
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1
    else:
        return sequence(x-2) + sequence(x-1)
# program pobiera N od uzytkownika i wypisuje N-ty element ciagu Fibonacciego  
num = int(input("type N to print Nth element of Fibonacci sequence (N is a number of your choice): "))
print(sequence(num))