# coding: utf-8

import sys
read = sys.stdin.readline
write = sys.stdout.write

def is_palindrom(numbers):
    idx = len(numbers)//2
    for i in range(1, idx+1):
        if numbers[i-1] != numbers[-i]:
            return "0"
    return "1"

n = int(input())
numbers = list(map(int, input().split()))

m = int(input())
result = []
for _ in range(m):
    s, e = map(int, read().split())
    p = is_palindrom(numbers[s-1:e])
    result.append(p)

for r in result:
    write(r)
    write("\n")

