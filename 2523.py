# coding: utf-8

n = int(input())

star = "*"

for i in range(1, n+1):
    print(star*i)

for i in range(n-1, 0, -1):
    print(star*i)
