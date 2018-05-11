# coding: utf-8


a, b = map(int, input().split())
n = int(input())

minimum = a * (1000 / b)
for _ in range(n):
    x, y = map(int, input().split())
    temp = x * (1000 / y)
    if temp < minimum:
        minimum = temp

print('{:.2f}'.format(minimum))
