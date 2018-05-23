# coding: utf-8 


n = int(input())

numbers = []

for _ in range(n):
    k = int(input())
    numbers.append(k)


for number in numbers:
    print('=' * number)

