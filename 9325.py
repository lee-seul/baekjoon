# coding: utf-8

n = int(input())

for _ in range(n):
    s = int(input())
    c = int(input())
    for _ in range(c):
        a, b = map(int, input().split())
        s += a*b
    print(s)

