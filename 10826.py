# coding: utf-8

n = int(input())


a = 0
b = 1
if n == 0:
    print(a)
if n == 1:
    print(b)
if n > 1:
    for _ in range(n-1):
        t = a + b
        a = b
        b = t
    print(b)
