# coding: utf-8

t = int(input())

for _ in range(t):
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(numbers[-3])

