# coding: utf-8

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    candy = list(map(int, input().split()))
    result = 0
    for c in candy:
        result += c // k
    print(result)

