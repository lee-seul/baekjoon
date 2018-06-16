# coding: utf-8


d = {chr(n+64):n for n in range(1, 27)}


n = int(input())
name = input()

result = 0
for c in name:
    result += d[c]

print(result)
