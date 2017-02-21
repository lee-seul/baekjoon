# coding: utf-8

n = int(input())

CY = 100
SD = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        CY -= b
    elif a > b:
        SD -= a

print(CY)
print(SD)
