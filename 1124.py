# coding: utf-8

from math import log

a, b = map(int, input().split())

numbers = [0 for i in range(b+1)]
for i in range(2, b+1):
    if numbers[i] <= 0:
        n = 2
        while i*n <= b:
            x = i * n
            while not x % i:
                numbers[i*n] += 1
                x /= i
            n += 1

result = 0
for i in range(a, len(numbers)):
    idx = numbers[i]
    if idx >= 2 and not numbers[idx]:
        result += 1

print(result)

