# coding: utf-8

import sys
write = sys.stdin.readline
n = int(input())
l = list(map(int, write().split()))
l.insert(0, 0)

result = [0 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(i):
        result[i] = max(result[i], result[j]+l[i-j])

print(result[n])
