# coding: utf-8


t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    
    m = int(input())

    result = [0 for _ in range(m+1)]
    result[0] = 1

    for coin in coins:
        for i in range(1, m+1):
            if i >= coin:
                result[i] += result[i-coin]

    print(result[-1])

