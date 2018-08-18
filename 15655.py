# coding: utf-8


from itertools import combinations


n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

result = list(combinations(numbers, m))

for r in result:
    r = map(str, r)
    print(' '.join(r))
