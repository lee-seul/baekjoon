# coding: utf-8

import sys
read = sys.stdin.readline

n = int(input())

result = 0
for _ in range(n):
    result += int(read())
    
result -= n - 1

print(result)

