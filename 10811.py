# coding: utf-8

n, m = map(int, input().split())


baskets = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    temp = baskets[i-1:j]
    temp.reverse()
    baskets[i-1:j] = temp

for i in range(n):
    print(baskets[i], end=" ")

