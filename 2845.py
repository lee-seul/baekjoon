# coding: utf-8

x, y = map(int, input().split())

att = x*y
result = []
new = list(map(int, input().split()))

for i in range(5):
    result.append(new[i] - att)

for i in range(5):
    print(result[i], end=" ")
