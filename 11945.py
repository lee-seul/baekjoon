# coding: utf-8

n, m = map(int, input().split())
result = []
for _ in range(n):
    temp = list(input())
    temp.reverse()
    result.append(temp)

for s in result:
    print("".join(s))

