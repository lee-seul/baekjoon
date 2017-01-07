# coding: utf-8


t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    y = n % h
    x = 1+n//h
    if y == 0:
        y = h
        x -= 1
    y *= 100
    print(y + x)
