# coding: utf-8


total = int(input())

price = []
for _ in range(9):
    price.append(int(input()))

print(total - sum(price))
