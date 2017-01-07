# coding: utf-8

from math import ceil

n = input()
count = [0 for i in range(10)]
for c in n:
    count[int(c)] += 1

count[6] += count[9]
count[6] = ceil(count[6] / 2)
count[9] = 0
print(max(count))
