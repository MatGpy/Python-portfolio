'''
kolko i krzyzyk:
1. wybierz tryb gry (sp - jeden gracz (gracz a - ty, gracz b - SI), mp - dwoch graczy (gracz a - osoba wybierajaca symbol, gracz b - druga osoba))
2. wybierz symbol, ktorym chcesz grac (x lub o)
3. gdy nadejdzie twoj ruch, wybierz miejsce na planszy, na ktorym chcesz umiescic swoj symbol wedlug wzoru: rk (r - rzad, k - kolumna)
4. gdy ktoremus z graczy uda sie ulozyc swoje 3 symbole w rownym rzedzie lub na skos, gra konczy sie jego zwyciestwem
5. gdy oboje gracze uloza swoje 3 symbole w rownym rzedzie lub na skos w tej samej rondzie, gra konczy sie remisem
6. gdy wszystkie pola na planszy sie zapelnia przed zwyciestwem ktoregos z graczy, gra konczy sie bez rozstrzygniecia
'''
import random
tryb = str(input("wybierz tryb gry: "))
sa = str(input("wybierz symbol a: "))
if sa == "x":
    sb = "o"
if sa == "o":
    sb = "x"
if sa != "x" and sa != "o":
    raise TypeError("cos poszlo nie tak")
t = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
    ]
i = 0
j = 0
k = 0
while t[0][0] != sa and t[0][1] != sa and t[0][2] != sa or t[0][0] != sb and t[0][1] != sb and t[0][2] != sb or t[1][0] != sa and t[1][1] != sa and t[1][2] != sa or t[1][0] != sb and t[1][1] != sb and t[1][2] != sb or t[2][0] != sa and t[2][1] != sa and t[2][2] != sa or t[2][0] != sb and t[2][1] != sb and t[2][2] != sb or t[0][0] != sa and t[1][1] != sa and t[2][2] != sa or t[0][0] != sb and t[1][1] != sb and t[2][2] != sb or t[0][2] != sa and t[1][1] != sa and t[2][0] != sa or t[0][2] != sb and t[1][1] != sb and t[2][0] != sb or t[0][0] != sa and t[1][0] != sa and t[2][0] != sa or t[0][0] != sb and t[1][0] != sb and t[2][0] != sb or t[0][1] != sa and t[1][1] != sa and t[2][1] != sa or t[0][1] != sb and t[1][1] != sb and t[2][1] != sb or t[0][2] != sa and t[1][2] != sa and t[2][2] != sa or t[0][2] != sb and t[1][2] != sb and t[2][2] != sb:
    a1 = str(input("ruch gracza a: "))
    t[int(a1[0])-1][int(a1[1])-1] = sa
    print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(t[0][0],t[0][1],t[0][2],t[1][0],t[1][1],t[1][2],t[2][0],t[2][1],t[2][2]))
    i = i+1
    if i == 9:
        print("koniec")
        break
    if tryb == "sp":
        b1 = random.randint(1,3)
        b2 = random.randint(1,3)
        while t[b1-1][b2-1] == "x" or t[b1-1][b2-1] == "o":
            b1 = random.randint(1,3)
            b2 = random.randint(1,3)
        t[b1-1][b2-1] = sb
        print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(t[0][0],t[0][1],t[0][2],t[1][0],t[1][1],t[1][2],t[2][0],t[2][1],t[2][2]))
    if tryb == "mp":
        b1 = str(input("ruch gracza b: "))
        t[int(b1[0])-1][int(b1[1])-1] = sb
        print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(t[0][0],t[0][1],t[0][2],t[1][0],t[1][1],t[1][2],t[2][0],t[2][1],t[2][2]))
        i = i+1
    if t[0][0] == sa and t[0][1] == sa and t[0][2] == sa or t[1][0] == sa and t[1][1] == sa and t[1][2] == sa or t[2][0] == sa and t[2][1] == sa and t[2][2] == sa or t[0][0] == sa and t[1][1] == sa and t[2][2] == sa or t[0][2] == sa and t[1][1] == sa and t[2][0] == sa or t[0][0] == sa and t[1][0] == sa and t[2][0] == sa or t[0][1] == sa and t[1][1] == sa and t[2][1] == sa or t[0][2] == sa and t[1][2] == sa and t[2][2] == sa:
        j = 1
    if t[0][0] == sb and t[0][1] == sb and t[0][2] == sb or t[1][0] == sb and t[1][1] == sb and t[1][2] == sb or t[2][0] == sb and t[2][1] == sb and t[2][2] == sb or t[0][0] == sb and t[1][1] == sb and t[2][2] == sb or t[0][2] == sb and t[1][1] == sb and t[2][0] == sb or t[0][0] == sb and t[1][0] == sb and t[2][0] == sb or t[0][1] == sb and t[1][1] == sb and t[2][1] == sb or t[0][2] == sb and t[1][2] == sb and t[2][2] == sb:
        k = 1
    if j+k == 1:
        if j == 1:
            print("gracz a wygrywa")
            break
        if k == 1:
            print("gracz b wygrywa")
            break
    if j+k == 2:
        print("remis")
        break
    if i > 9:
        print("koniec")
        break