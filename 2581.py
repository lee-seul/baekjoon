# coding: utf-8

import math

m = int(input())
n = int(input())

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

l = []
for i in range(m, n+1):
    if is_prime(i):
        l.append(i)

if len(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(min(l))



