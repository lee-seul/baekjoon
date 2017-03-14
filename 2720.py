# coding: utf-8

t = int(input())
coins = [25, 10, 5, 1]

for _ in range(t):
    c = int(input())
    result = []
    for coin in coins:
        num = c // coin
        result.append(num)
        c -= num * coin
    for r in result:
        print(r, end=" ")
    print()
