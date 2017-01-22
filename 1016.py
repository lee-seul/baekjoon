# coding: utf-8

import math

mi, ma = map(int, input().split())


numbers = set(range(mi, ma + 1))
for i in range(2, math.floor(ma ** 0.5) + 1):
    square = i ** 2
    numbers -= set(range(math.ceil(mi / square) * square, ma + 1, square))

print(len(numbers))

