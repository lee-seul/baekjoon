# coding: utf-8 


t = int(input())

for _ in range(t):
    price = float(input())
    price *= 0.8

    print('${:.2f}'.format(price))
