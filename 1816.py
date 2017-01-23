# coding: utf-8

def is_primes(num, primes):
    for prime in primes:
        if not num % prime:
            return False
    return True

ma = 10**6

numbers = [0 for _ in range(ma)]

for i in range(2, ma):
    if not numbers[i]:
        n = 2
        while i * n < ma:
            numbers[i*n] = 1
            n += 1

primes = [i for i in range(2, ma) if not numbers[i]]

n = int(input())
result = []

for _ in range(n):
    s = int(input())
    if is_primes(s, primes):
        result.append(1)
    else:
        result.append(0)

for e in result:
    if e:
        print("YES")
    else:
        print("NO")
