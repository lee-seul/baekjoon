# coding: utf-8


n = int(input())

if n < 2:
    print(0)
else:
    result = 2 * (3 ** (n-2))
    print(result % 1000000009)
