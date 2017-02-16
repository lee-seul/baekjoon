# coding: utf-8

KOI = list(map(int, input().split()))

result = 0
for num in KOI:
    result += num ** 2

print(result % 10)

