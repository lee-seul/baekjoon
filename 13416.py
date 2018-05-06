# coding: utf-8


t = int(input())

for _ in range(t):
    n = int(input())
    result = 0
    for _ in range(n):
        data = list(map(int, input().split()))
        data.sort()
        if data[2] > 0:
            result += data[2]
    print(result)
