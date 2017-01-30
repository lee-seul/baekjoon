# coding: utf-8

from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input()) 
    alc = Counter()
    for _ in range(n):
        uni, amount = input().split()
        alc.update({uni:int(amount)})
    print(alc.most_common(1)[0][0])
