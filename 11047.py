# coding: utf-8

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

coins.reverse()

ans = 0
for coin in coins:
    if k >= coin:
        ans += k // coin
        k = k % coin

print(ans)

