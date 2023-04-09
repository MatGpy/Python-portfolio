# Program sprawdzajacy czy dana liczba jest palindromem
# program definiuje funkcje sprawdzajaca czy liczba jest palindromem
def palindrom(x):
    # funkcja zamienia liczbe podana na wejsciu na stringa
    string1 = str(x)
    j = 0
    i = 0
    length = len(string1)-1
    # funkcja posluguje sie petla while, aby sprawdzic, czy znaki po przeciwnych stronach stringa sa identyczne. Gdy tak jest, iterator zwiekszany jest o 1, tak samo jak waryosc zmiennej m
    while string1[i] == string1[length-i]:
          j = j+1
          i = i+1
          # program konczy dzialanie petli w przypadku, w którym iterator osiaga wartosc wyzsza niz dlugosc badanego stringa
          if i > length:
             break
    # funkcja sprawdza, czy wartosc zmiennej m jest rowna dlugosci badanego stringa (wartosc m byla zwiekszana o 1 za kazdym razem, kiedy znaki po przeciwnych stronach stringa byly identyczne. Dlatego zakladajac, ze petla przeszla przez calego stringa, liczba w stringu jest palindromem wylacznie wtedy, gdy wartosc m jest rowna dlugosci tego stringa)
    if j == len(string1):
       return "your number is a palindrome"
    else:
       return "your number isn't a palindrome"
# program pobiera od uzytkownika liczbe, ktora uzytkownik chce zbadac, a nastepnie zwraca odpowiednia odpowiedz w zaleznosci od tego, czy podana liczba jest palindromem      
number = int(input("type a number: \n"))
print(palindrom(number))