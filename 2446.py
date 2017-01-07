# coding: utf-8

n = int(input())

l = list(range(n, 0, -1)) + list(range(2, n+1))
for i in l:
    s = "*" * (2*i-1)
    print(s.rjust(n+i-1))

