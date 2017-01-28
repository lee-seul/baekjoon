# coding: utf-8


a, b = map(int, input().split())

numbers = [0 for i in range(b+1)]
for i in range(2, b+1):
    if not numbers[i]:
        n = 2
        while i*n <= b:
            numbers[i*n] = 1
            n += 1

# primes = [i for i in range(2, b+1) if not numbers[i]]
# tests = [i for i in range(a, b+1) if numbers[i]]
primes = []
tests = []
for i in range(2, b+1):
    if numbers[i]:
        tests.append(i)
    else:
        primes.append(i)

result = 0
for i in tests:
    print(i)
    cnt = 0
    j = 0
    n = i
    while n != 1:
        if not n % primes[j]:
            cnt += 1
            n /= primes[j]
        else:
            j += 1
    if cnt in primes:
        result += 1

print(result)
            
