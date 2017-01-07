# coding: utf-8

T = int(input())

l = []
for i in range(T):
    l.append(input().split())

for i in range(T):
    result = ""
    for c in l[i][1]:
        result += c * int(l[i][0])
    print(result)


