# coding: utf-8

k = int(input())

for _ in range(k):
    p, m = map(int, input().split())
    seats = [0 for _ in range(m)]
    result = 0
    for _ in range(p):
        n = int(input())
        if seats[n-1]:
            result += 1
        seats[n-1] = 1
    print(result)

