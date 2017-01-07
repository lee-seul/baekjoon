# coding: utf-8

a, b = map(int, input().split())

result = []
n = 1
while len(result) <= b:
    for _ in range(1, n+1):
        result.append(n)
    n+=1

print(sum(result[a-1:b]))

