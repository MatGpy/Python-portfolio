# This program replaces all diacritics in a string from the user's input
# program takes a string from the user's input
string1 = str(input("type a word/sentence you want to edit:"))
# program creates a dictionary with diacritics and signs these diacritics will be replaced with and an empty string
diacritics = {"ą": "a", "ę": "e", "ł": "l", "ś": "s", "ż": "z", "ó": "o", "ź": "z", "ń": "n", "ć": "c", "Ą": "A", "Ę": "E", "Ł": "L", "Ś": "S", "Ż": "Z", "Ó": "O", "Ź": "Z", "Ń": "N", "Ć": "C"}
string2 = ""
i = 0
# program creates a loop which moves string from the input to the empty string created earlier and replaces diacritics in the meantime
while i < len(string1):
    if string1[i] in diacritics:
        string2 = string2+diacritics[string1[i]]
    else:
        string2 = string2+string1[i]
    i = i+1
# program outputs modified strings
print(string2)
