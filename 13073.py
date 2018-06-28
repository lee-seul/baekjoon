# coding: utf-8


t = int(input())

for _ in range(t):
    n = int(input())
    result = sum(list(range(n+1)))

    print(result, result*2-n, result*2)
