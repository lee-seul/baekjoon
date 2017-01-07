# coding: utf-8

s = input()
result = ""
for c in s:
    if ord(c) >= 65 and ord(c) <= 90:
        result += chr(ord(c)+32)
    elif ord(c) >= 97 and ord(c) <= 122:
        result += chr(ord(c)-32)
print(result)
