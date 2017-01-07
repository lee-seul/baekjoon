# coding: utf-8

n = int(input())
a = n*2 -1
for i in range(n, 0, -1):
    s = "*" * (2 * i -1)
    print(s.rjust(a))
    a -= 1

