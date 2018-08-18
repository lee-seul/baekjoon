# coding: utf-8 


from itertools import combinations

n, m = map(int, input().split())
result = combinations(range(1, n+1), m)

for r in result:
    r = map(str, r)
    print(' '.join(r))
