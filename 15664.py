# coding: utf-8


from itertools import combinations


n, m = map(int, input().split())
numbers = [int(x) for x in input().split()]
numbers.sort()

result = set(combinations(numbers, m))
result = list(result)
result.sort()

for r in result:
    r = [str(x) for x in r]
    print(' '.join(r))

