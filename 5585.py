# coding: utf-8

coins = [500, 100, 50, 10, 5, 1]

result = 0
change = 1000 - int(input())
i = 0
while change:
    if change >= coins[i]:
        result += 1
        change -= coins[i]
    else:
        i += 1

print(result)

