# coding: utf-8

from math import sqrt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))+1):
        if not num % i:
            return False
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    
    result = n // 2
    if is_prime(result):
        print(result, result)
        continue
    for i in range(1, result):
        if is_prime(result + i) and is_prime(result - i):
            print(result - i, result + i)
            break
