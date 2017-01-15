# coding: utf-8

s = input()
cam = "CAMBRIDGE"

result = ""
for c in s:
    if c not in cam:
        result += c

print(result)
