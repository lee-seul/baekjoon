# coding: utf-8

year = int(input())

result = 0
if not year % 4 and year % 100:
    result = 1
if not year % 400:
    result = 1

print(result)

