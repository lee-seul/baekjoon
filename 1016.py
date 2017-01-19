# coding: utf-8

mi, ma = map(int, input().split())

numbers = [0 for _ in range(ma+1)]

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
