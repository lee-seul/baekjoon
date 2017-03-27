# coding: utf-8

k = int(input())

result = []
for _ in range(k):
    n = int(input())
    if not n:
        result.pop()
    else:
        result.append(n)

print(sum(result))

