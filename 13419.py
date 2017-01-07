# coding: utf-8

n = int(input())

for _ in range(n):
    s = input()
    if len(s) % 2 != 0:
        s *= 2 
    first = ""
    second = ""
    for i in range(len(s)):
        if i % 2 == 0:
            first += s[i]
        else:
            second += s[i]
    print(first)
    print(second)


