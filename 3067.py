# coding: utf-8


t = int(input())

for _ in range(t):
    n = int(input())
    kind = list(map(int, input().split()))
    amount = int(input())
    coins = [0 for _ in range(amount+1)]
    coins[0] = 1
    for i in range(1, amount+1):
        for coin in kind:
            if i-coin >= coin:
                coins[i] += 1
            else:
                coins[i] = coins[i-1]
            print(coins)
    print(coins[amount])

