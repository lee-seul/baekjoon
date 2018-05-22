# coding: utf-8


from math import log


n = int(input())

if n == 1:
    print(n)
else:
    digit = int(log(n, 2))
    std = 2 ** (digit+1)
    if std//2 == n:
        print(n)
    else:
        gap = std - n
        result = std - 2 * gap
        print(result) 
