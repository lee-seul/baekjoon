# coding: utf-8

from math import ceil, sqrt
n = int(input())

for i in range(ceil(sqrt(n))+1):
    if n < i **2:
        print(i-1)
        break
    elif n == i**2:
        print(i)
        break
