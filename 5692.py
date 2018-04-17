# coding: utf-8

import sys


fac = [1, 2, 6, 24, 120]

while True:
    n = sys.stdin.readline().strip()
    if n == '0':
        break 
    n = list(n)
    n.reverse()

    result = 0
    for i, num in enumerate(n):
        result += int(num) * fac[i]
    
    sys.stdout.write(str(result) + '\n')

