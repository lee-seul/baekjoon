# coding: utf-8

from math import sqrt, ceil


def find_primes(num):
    numbers = [0 for _ in range(num+1)]
    for i, e in enumerate(numbers):
        if i < 2:
            continue
        if e == 0:
            n = 2
            while i*n <= num:
                numbers[i*n] = 1
                n += 1
    primes = [i for i in range(2, num+1) if numbers[i]]
    return primes 


mi, ma = map(int, input().split())

length = ma - mi + 1
numbers = [0 for _ in range(length)]

primes = find_primes(ma)

i = 2
while i ** 2 <= ma:
    idx = i ** 2
    if not numbers[idx]:
        n = 1
        while idx * n <= ma:
            numbers[idx*n] = 1
            n+= 1
    i += 1

print(numbers[1:].count(0))
