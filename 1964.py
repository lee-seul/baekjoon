# coding: utf-8

n = int(input())
result = 5
plus = 7
for _ in range(n-1):
    result += plus
    plus += 3

print(result%45678)

