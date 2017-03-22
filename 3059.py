# coding: utf-8

n = int(input())

for _ in range(n):
    s = input()
    result = 2015
    s = set(s)
    for c in s:
        result -= ord(c)
    print(result)

