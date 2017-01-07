# coding: utf-8

s = "*"
n = int(input())

l = list(range(1, n+1) )+ list(range(n-1, 0, -1))

for i in l:
    a = (s*i).ljust(n) + (s*i).rjust(n)
    print(a)
    


