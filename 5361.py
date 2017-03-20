# coding: utf-8

price = [350.34, 230.90, 190.55, 125.30, 180.90]

t = int(input())
for _ in range(t):
    parts = list(map(int, input().split()))
    result = 0
    for i in range(5):
        result += parts[i] * price[i]
    print("${:.2f}".format(result))

