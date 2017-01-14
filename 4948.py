# coding: utf-8

def count_prime(num):
    sieve = [0 for _ in range(2*num+1)]
    for i in range(2, 2*num+1):
        if not sieve[i]:
            n = 2
            while i * n <= 2*num:
                sieve[i*n] = 1
                n += 1
    return sieve[num+1:].count(0)

while True:
    n = int(input())
    if not n:
        break
    print(count_prime(n)) 
