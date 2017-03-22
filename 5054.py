# coding: utf-8

t = int(input())

for _ in range(t):
    n = int(input())
    stores = list(map(int, input().split()))
    stores.sort()
    print((stores[-1] - stores[0]) * 2)

