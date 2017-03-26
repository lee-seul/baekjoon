# coding: utf-8

import sys
read = sys.stdin.readline

t = int(read())

result = [0, 0]
for _ in range(t):
    a, b = map(int, read().split())
    if a > b:
        result[0] += 1
    elif a < b:
        result[1] += 1

print(result[0], result[1])
