# coding: utf-8 

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    result = 0
    for _ in range(n):
        v, f, c = map(int, input().split())
        temp = v * (f / c)
        if temp >= d:
            result += 1
    print(result)
