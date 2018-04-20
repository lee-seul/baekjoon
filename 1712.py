# coding: utf-8


a, b, c = map(int, input().split())

profit = c - b
if profit <= 0:
    print(-1)
else:
    print(a//profit + 1)

