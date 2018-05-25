# coding: utf-8

a, b = map(int, input().split())
price = int(input()) * 2


if a+b >= price:
    print(a+b - price)
else:
    print(a+b)
