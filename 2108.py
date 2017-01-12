# coding: utf-8

import sys
from collections import Counter

n = int(input())
values = [0 for _ in range(n)]

for i in range(n):
    values[i] = int(sys.stdin.readline())
    
values.sort()

c = Counter(values)
max_count = c.most_common(1)[0][1]
result = []
for key in c.keys():
    if c[key] == max_count:
        result.append(key) 

result.sort()
if len(result) > 1:
        result.pop(0)

print("{:.0f}".format(sum(values)/n))
print(values[(n+1)//2-1])
print(result[0])
print(values[-1] - values[0])
