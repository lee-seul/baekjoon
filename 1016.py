# coding: utf-8


def find_primes(num):
    numbers = [0 for _ in range(num+1)]
    for i, e in enumerate(numbers):
        if i < 2:
            continue
        if  not e:
            n = 2
            while i*n <= num:
                numbers[i*n] = 1
                n += 1
    primes = [i for i in range(2, num+1) if not numbers[i]]
    return primes


mi, ma = map(int, input().split())

length = ma - mi + 1
numbers = [0 for _ in range(length+1)]
numbers[0] = 1

primes = find_primes(int(ma ** 0.5))

for prime in primes:
    for i, e in enumerate(numbers):
        if not (mi + i - 1) % (prime ** 2) and not e:
            n = 1
            while i*n <= length:
                numbers[i*n] = 1
                n += 1
            break

print(numbers.count(0))
            
