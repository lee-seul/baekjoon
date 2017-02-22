# coding: utf-8

n = int(input())

cards = [x for x in range(1, n+1)]

while cards:
    print(cards.pop(0), end=" ")
    if cards:
        cards.append(cards.pop(0))
