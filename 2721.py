# coding: utf-8 


def td(n):
    return sum([i+1 for i in range(n)])


def wd(n):
    return sum([k*td(k+1) for k in range(1, n+1)])


t = int(input())

for _ in range(t):
    n = int(input())
    print(wd(n))
