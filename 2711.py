# coding: utf-8

t = int(input())

for _ in range(t):
    n, st = input().split()
    n = int(n)
    print(st[:n-1] + st[n:])

