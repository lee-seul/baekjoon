# coding: utf-8

from math import log

a, b = map(int, input().split())

primes = []
numbers = [0 for i in range(b+1)]
for i in range(2, b+1):
    if not numbers[i]:
        n = 2
        primes.append(i)
        while i*n <= b:
            print(i, numbers)
            if not n % i:
                if log(n, i) == int(log(n, i)):
                    x = log(i*n, i)
                else:
                    x = numbers[n]
            else:
                x = 1
            print(x)
            numbers[i*n] += x
            n += 1


result = 0
for i in range(2, len(numbers)):
    print(i, numbers[i])
    idx = int(numbers[i])
    if not numbers[idx] and idx >= 2:
        result += 1

print(result)

