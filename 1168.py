# coding: utf-8

import sys
write = sys.stdout.write

n, m = map(int, input().split())

people = [x for x in range(1, n+1)]
result = []

idx = m - 1
while len(result) < n:
    result.append(str(people.pop(idx)))
    idx += m - 1
    if len(people):
        idx %= len(people)

write("<" + ", ".join(result) + ">")
