# coding: utf-8


import math
from decimal import Decimal


def cal(a, b, c):
    if a == -1:
        if b >= c:
            return -1
        return 'a', math.sqrt(c**2 - b ** 2)
    
    if b == -1:
        if a >= c:
            return -1
        return 'b', math.sqrt(c**2 - a ** 2)

    if c == -1:
        return 'c', math.sqrt(a ** 2 + b ** 2)


idx = 1
while True:
    a, b, c = map(int, input().split())
    if not a and not b and not c:
        break 

    print(f'Triangle #{idx}')
    result = cal(a, b, c)

    if result == -1:
        result = 'Impossible.'
        print(result)
    else:
        value = Decimal(result[1])
        print(f'{result[0]} = {value:.3f}')
    
    print()
    idx += 1

