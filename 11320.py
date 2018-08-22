# coding: utf-8

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    c = a // b
    print(c**2)
