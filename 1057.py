# coding: utf-8

from math import ceil 

n, a, b = map(int, input().split())

result = 1
while ceil(a/2) != ceil(b/2):
    a = ceil(a/2)
    b = ceil(b/2)
    result += 1

print(result)




