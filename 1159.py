# coding: utf-8

n = int(input())

alp = [0 for _ in range(26)]

for _ in range(n):
    name = input()
    idx = ord(name[0]) - 97
    alp[idx] += 1


result = ""
for i in range(26):
    if alp[i] >= 5:
        a = chr(i+97)
        result += a

if not result:
    result = "PREDAJA"

print(result)

