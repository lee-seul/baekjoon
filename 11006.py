# coding: utf-8

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    u = m * 2 - n
    T = m - u
    print(u, T)

