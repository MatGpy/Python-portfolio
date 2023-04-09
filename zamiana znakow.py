# Program sluzacy do usuwania znakow diakrytycznych z tekstu podanego przez uzytkownika
# program pobiera od uzytkownika stringa, ktorego nalezy przerobic
string1 = str(input("wpisz zdanie, ktore chcesz zamienic:"))
# program tworzy slownik ze znakami diakrytycznymi i znakami, ktorymi maja byc one zastepowane, oraz pustego stringa
diacritics = {"ą": "a", "ę": "e", "ł": "l", "ś": "s", "ż": "z", "ó": "o", "ź": "z", "ń": "n", "ć": "c", "Ą": "A", "Ę": "E", "Ł": "L", "Ś": "S", "Ż": "Z", "Ó": "O", "Ź": "Z", "Ń": "N", "Ć": "C"}
string2 = ""
i = 0
# program tworzy petle, ktora przenosi stringa podanego przez uzytkownika do nowego stringa, jednoczesnie zastepujac znaki diakrytyczne ich "normalniejszymi" odpowiednikami
while i < len(string1):
    if string1[i] in diacritics:
        string2 = string2+diacritics[string1[i]]
    else:
        string2 = string2+string1[i]
    i = i+1
# program wyswietla przerobionego stringa
print(string2)
