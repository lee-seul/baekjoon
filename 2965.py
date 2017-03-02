# coding: utf-8

a, b, c = map(int, input().split())

if b - a >= c - b:
    print(b - a - 1)
else:
    print(c - b - 1)

