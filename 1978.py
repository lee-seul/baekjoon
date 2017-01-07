# coding: utf-8

import math

n = int(input())
l = map(int, input().split())

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

cnt = 0
for i in l:
    if is_prime(i):
        cnt += 1
print(cnt)

