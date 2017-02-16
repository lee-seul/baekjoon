# coding: utf-8

n = int(input())

for _ in range(n):
    a = int(input())
    numbers = list(map(int, input().split()))
    print(sum(numbers))

