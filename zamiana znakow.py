a = str(input("wpisz zdanie, ktore chcesz zamienic:"))
b = {"ą": "a", "ę": "e", "ł": "l", "ś": "s", "ż": "z", "ó": "o", "ź": "z", "ń": "n", "ć": "c", "Ą": "A", "Ę": "E", "Ł": "L", "Ś": "S", "Ż": "Z", "Ó": "O", "Ź": "Z", "Ń": "N", "Ć": "C"}
c = ""
i = 0
while i < len(a):
    if a[i] in b:
        c = c+b[a[i]]
    else:
        c = c+a[i]
    i = i+1
print(c)
