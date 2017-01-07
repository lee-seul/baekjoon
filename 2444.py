# coding: utf-8

n = int(input())
a = n
for i in range(1, n+1):
    s = "*" * (i*2 -1)
    print(s.rjust(a))
    a += 1

a = n*2-2
for i in range(n-1, 0, -1):
    s = "*" * (i* 2 -1)
    print(s.rjust(a))
    a -= 1

