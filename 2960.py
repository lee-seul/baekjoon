# coding: utf-8


def ara(num, k):
    primes = []
    numbers = [0 for _ in range(num+1)]
    for i in range(2, num+1):
        if not numbers[i]:
            n = 1
            while i * n <= num:
                if not numbers[i*n]: 
                    primes.append(i*n)
                    numbers[i*n] = 1
                n += 1
        if len(primes) >= k:
            break
    return primes[k-1]
                

n, k = map(int, input().split())

print(ara(n, k))
