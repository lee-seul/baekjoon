# coding: utf-8


vowel = ['a', 'e', 'i', 'o', 'u']

string = input()
result = ""

string = list(string)

while string:
    c = string.pop(0)
    result += c
    if c in vowel:
        string.pop(0)
        string.pop(0)

print(result)

