# coding: utf-8

n = int(input())

l = []
for i in range(n):
    l.append(input())

for i in range(n):
    k = l[i].split("X")
    result = 0
    for s in k:
        for j in range(len(s)):
            result += j+1
    print(result)

