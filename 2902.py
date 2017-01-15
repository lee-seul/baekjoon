# coding: utf-8

s = input()
result = s[0]

for i, c in enumerate(s):
    if c == '-':
        result += s[i+1]
print(result)
