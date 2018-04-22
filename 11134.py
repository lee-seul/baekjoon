# coding: utf-8

from math import ceil


t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    print(ceil(n/c))
