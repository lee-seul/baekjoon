# coding: utf-8


from itertools import permutations


n, m = map(int, input().split())
numbers = map(int, input().split())

result = list(permutations(numbers, m))
result.sort()

for r in result:
    r = map(str, r)
    print(' '.join(r))
