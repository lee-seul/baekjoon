# coding: utf-8

m, n = map(int, input().split())

baskets = [x for x in range(1, m+1)]

for _ in range(n):
    i, j = map(int, input().split())
    tmp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = tmp

for i in range(m):
    print(baskets[i], end=" ")
