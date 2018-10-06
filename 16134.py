# coding: utf-8


from itertools import combinations

a, b = map(int, input().split())
print(len(list(combinations(range(a), b))))
