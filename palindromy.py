# Program sprawdzajacy czy dana liczba/slowo jest palindromem
# program definiuje funkcje sprawdzajaca czy liczba/slowo jest palindromem
def palindrom(x):
    j = 0
    i = 0
    length = len(x)-1
    # funkcja posluguje sie petla while, aby sprawdzic, czy znaki po przeciwnych stronach stringa sa identyczne. Gdy tak jest, iterator zwiekszany jest o 1, tak samo jak waryosc zmiennej m
    while x[i] == x[length-i]:
          j = j+1
          i = i+1
          # program konczy dzialanie petli w przypadku, w ktorym iterator osiaga wartosc wyzsza niz dlugosc badanego stringa
          if i > length:
             break
    # funkcja sprawdza, czy wartosc zmiennej m jest rowna dlugosci badanego stringa (wartosc m byla zwiekszana o 1 za kazdym razem, kiedy znaki po przeciwnych stronach stringa byly identyczne. Dlatego zakladajac, ze petla przeszla przez calego stringa, liczba w stringu jest palindromem wylacznie wtedy, gdy wartosc m jest rowna dlugosci tego stringa)
    if j == len(x):
       return "{} is a palindrome".format(x)
    else:
       return "{} isn't a palindrome".format(x)
# program pobiera od uzytkownika liczbe/slowo, ktora uzytkownik chce zbadac, a nastepnie zwraca odpowiednia odpowiedz w zaleznosci od tego, czy podana liczba/slowo jest palindromem      
input = str(input("type a number/word: \n"))
print(palindrom(input))