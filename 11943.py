# coding: utf-8

a, b = map(int, input().split())
c, d = map(int, input().split())

if a + d >= c + b:
    print(c + b)
else:
    print(a + d)

