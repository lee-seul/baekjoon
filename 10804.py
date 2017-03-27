# coding: utf-8

cards = [i for i in range(1, 21)]

for _ in range(10):
    i, j = map(int, input().split())
    temp = cards[i-1:j]
    temp.reverse()
    cards[i-1:j] = temp

for card in cards:
    print(card, end=" ")

