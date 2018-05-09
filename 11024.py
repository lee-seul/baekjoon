# coding: utf-8


t = int(input())

for _ in range(t):
    numbers = list(map(int, input().split()))
    print(sum(numbers))
