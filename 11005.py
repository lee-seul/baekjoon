# coding: utf-8

from math import log


digit = {x:str(x) for x in range(10)}
digit.update({x-55:chr(x) for x in range(65, 91)})

num, c = map(int, input().split())
max_digit = int(log(num, c))

result = ""
for i in range(max_digit, -1, -1):
    temp = num // (c ** i)
    result += digit[temp]
    num -= temp * (c ** i)

print(result)

