"""
Generator zamowien na komputery - program ten generuje losowe zamowienie na komputer lub caly zestaw komputerowy z peryferiami, z nowych lub uzywanych czesci, w okreslonym budzecie, do okreslonych zadan, spelniajacy konkretne wymagania, posiadajacy konkretne funkcje. Program ten napisalem w celu sprawdzenia swoich umiejetnosci w ukladaniu komputerow w okreslonym budzecie i do okreslonego przeznaczenia.
"""
# program tworzy funkcje wybierajaca, czy zestaw ma skladac sie wyacznie z komputera, czy z komputera wraz z peryferiami
def func1(b):
 if b == 1:
    return "PC"
 if b == 2:
    return "PC + peripherals"
# program tworzy funkcje wybierajaca, czy zestaw ma sie skladac z nowych, czy z uzywanych czesci
def func2(c):
 if c == 1:
    return "only new parts"
 if c == 2:
    return "new parts or used parts"
# program tworzy funkcje wybierajaca przeznaczenie zestawu
def purpose(d, a):
 if d == 1:
    return "gaming"
 if d == 2:
    return "productivity"
 if d == 3:
    return "streaming"
 if d == 4 and a <= 3000:
    return "NAS"
 if d == 4 and a > 3000:
    return "mixed"
 if d == 5 and a <= 3000:
    return "office tasks"
 if d == 5 and a > 3000:
    return "mixed"
 if d == 6: 
    return "mixed"
 if d == 7 and a <= 3000:
    return "HTPC"
 if d == 7 and a > 3000:
    return "mixed"
 if d == 8:
    return "mixed"
# program tworzy funkcje wybierajaca typ gier, do ktorych ma byc przeznaczony komputer w przypadku, w ktorym zestaw ma byc przeznaczony do grania, lub wybierajaca konkretne zastosowanie produktywne w przypadku, w ktoeym komp[uter ma sluzyc do zastosowan produktywnych
def priority2(e, d):
 if e == 1 and d == 1:
    return "RTS"
 if e == 2 and d == 1:
    return "racing games"
 if e == 3 and d == 1:
    return "FPS games"
 if e == 4 and d == 1:
    return "RPG games"
 if e == 5 and d == 1:
    return "newest AAA titles in 4k"
 if e == 6 and d == 1:
    return "mixed"
 if e == 7 and d == 1:
    return "newest AAA titles in 1080p"
 if e == 8 and d == 1:
    return "e-sport titles"
 if e == 9 and d == 1:
    return "open world games"
 if e == 10 and d == 1:
    return "newest AAA titles in 1440p"
 if e == 11 and d == 1:
    return "mixed"
 if e == 1 and d == 2:
    return "photo editing"
 if e == 2 and d == 2:
    return "2D modeling"
 if e == 3 and d == 2:
    return "Video editing"
 if e == 4 and d == 2:
    return "programming"
 if e == 5 and d == 2:
    return "mixed"
 if e == 6 and d == 2:
    return "mixed"
 if e == 7 and d == 2:
    return "animations making"
 if e == 8 and d == 2:
    return "AI / machine learning"
 if e == 9 and d == 2:
    return "music production"
 if e == 10 and d == 2:
    return "CAD"
 if e == 11 and d == 2:
    return "3D modeling"
 else:
    return "mixed"
# program tworzy funkcje precyzujaca wymagania odnosnie glosnosci pracy zestawu
def noise(g):
 if g == 1:
     return "it's neutral for me"
 if g == 2:
     return "it should be as quiet as possible"
 if g == 3:
     return "not too loud, but it doesn't have to be really quiet"
 if g == 4:
     return "I play with headphones"
 if g == 5:
     return "every additional db is painful"
 if g == 6:
     return "it's neutral for me"
 if g == 7:
     return "it's neutral for me"
# program tworzy funkcje precyzujaca wymagania odnosnie temperatury pracy zestawu
def cooling(h):
 if h == 1:
    return "it must be as cool as possible"
 if h == 2:
    return "it's neutral for me"
 if h == 3:
    return "If it won't achieve temperature of sun, I will be satisfied"
 if h == 4:
    return "it's neutral for me"
# program tworzy funkcje precyzujaca wymagania odnosnie wymiarow komputera    
def size(l):
 if l == 1:
    return "as small as possible"
 if l == 2:
    return "small PCs are nice, but temperatures are more important"
 if l == 3:
    return "small, but not too small"
 if l == 4:
    return "i like normal-sized PCs"
 if l == 5:
    return "small PCs are nice, but cost is more important"
 if l == 6:
    return "it's neutral for me"
 if l == 7:
    return "i like normal-sized PCs"
 if l == 8:
    return "it's neutral for me"
# program tworzy funkcje wybierajaca preferencje odnosnie kolorystyki komputera i jego oswietlenia
def aesthetics(i):
 if i == 1:
    return "Black theme with lots of RGB"
 if i == 2:
    return "Black theme without RGB"
 if i == 3:
    return "White theme without RGB"
 if i == 4:
    return "Black theme with some RGB"
 if i == 5:
    return "White theme with some RGB"
 if i == 6:
    return "It isn't important for me"
 if i == 7:
    return "It isn't important for me"
 if i == 8:
    return "White theme with lots of RGB"
# program tworzy funkcje wybierajaca, na ktory obszar zestawu nalezy zwrocic najwieksza uwage    
def priority(m, b):
 if m == 1 and b == 2:
     return "better pc"
 if m == 2 and b == 2:
     return "better monitor"
 if m == 3 and b == 2:
     return "better peripherals"
 if m == 1 and b == 1:
     return "better specs"
 if m == 2 and b == 1:
     return "better looks"
 if m == 3 and b == 1:
     return "silence"
# program tworzy funkcje wybierajaca preferencje odnosnie tego, ktore peryferia maja byc przewodowe, a ktore bezprzewodowe (w przypadku, w ktorym peryferia maja byc dodane do zestawu)
def peripherals(r, b):
 if r == 1 and b == 2:
     return "all peripherals wired"
 if r == 2 and b == 2:
     return "mouse wireless, other peripherals wired"
 if r == 3 and b == 2:
     return "mouse and keyboard wireless, headphones wired"
 if r == 4 and b == 2:
     return "all peripherals wireless"
 if r == 5 and b == 2:
     return "all peripherals wired"
 if r == 6 and b == 2:
     return "it's neutral for me"
 if r == 7 and b == 2:
     return "it's neutral for me"
 else:
     return "no peripherals"
# program tworzy funkcje wybierajaca ewentualne zyczenia uzytkownika dotyczace zestawu     
def special_wishes(j, k, b):
 if j == 1 or k == 1:
     return "none"
 if j == 2 or k == 2:
     return "minimum 2tb of system memory"
 if j == 3 or k == 3:
     return "minimum 3tb of system memory"
 if j == 4 or k == 4:
     return "minimum 16gb of ram"
 if j == 5 or k == 5:
     return "none"
 if j == 6 and b == 2 or k == 6 and b == 2:
     return "ultrawide monitor"
 if j == 7 and b == 2 or k == 7 and b == 2:
     return "monitor with 144 hz of refresh rate"
 if j == 8 or k == 8:
     return "none"
 if j == 9 and b == 2 or k == 9 and b == 2:
     return "monitor with 4k resolution"
 if j == 10 or k == 10:
     return "more than 1tb of system memory"
 if j == 11 or k == 11:
     return "none"
 if j == 12 or k == 12:
     return "none"
 if j == 13 or k == 13:
     return "minimum 32gb of RAM"
 if j == 14 and b == 2 or k == 14 and b == 2:
     return "monitor with wqhd resolution"
 if j == 15 or k == 15:
     return "support for RT"
 if j == 16 and b == 2 or k == 16 and b == 2:
     return "two monitors"
 if j == 17 and b == 2 or k == 17 and b == 2:
     return "three monitors"
 if j == 18 or k == 18:
     return "only SSD storage"
 if j == 19 or k == 19:
     return "none"
 if j == 20 or k == 20:
     return "none"
 if j == 21 or k == 21:
     return "none"
 if j == 22 or k == 22:
     return "none"
 if j == 23 and b == 2 or k == 23 and b == 2:
     return "monitor with 240 hz of refresh rate"
 if j == 24 or k == 24:
     return "none"
# program tworzy funkcje wybierajaca, czy uzytkownik bedzie chcial podkrecac zamowiony komputer
def overclocking(h):
 if h == 1:
     return "I want to OC"
 if h == 2:
     return "I don't want to OC"
 if h == 3:
     return "it's neutral for me"
 if h == 4:
     return "it's neutral for me"
# program tworzy zbior losowo wygenerowanych liczb, ktore beda potrzebne do wygenerowania zamowienia
import random
a = random.randint(1000,18000)
b = random.randint(1,2)
c = random.randint(1,2)
d = random.randint(1,8)
e = random.randint(1,13)
g = random.randint(1,7)
h = random.randint(1,4)
i = random.randint(1,8)
j = random.randint(1,23)
k = random.randint(1,23)
l = random.randint(1,8)
m = random.randint(1,3)
r = random.randint(1,7)
# program wstawia losowo wygenerowane liczby do funkcji i wyswietla wykonane w ten sposob zamowienie na zestaw komputerowy
print("price:\n{}\n\n{}\n{}\n\npurpose:\n{}\n{}\n\npriority:\n{}\n\nnoise:\n{}\n\ncooling:\n{}\n\naesthetics:\n{}\n\nsize:\n{}\n\npriority:\n{}\n\nperipherals:\n{}\n\nOC:\n{}\n\nspecial wishes:\n{}\n".format(a,func1(b),func2(c),purpose(d,a),priority2(e,d),priority(m,b),noise(g),cooling(h),aesthetics(i),size(l),priority(m,b),peripherals(r,b),overclocking(h),special_wishes(j,k,b)))