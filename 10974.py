# coding: utf-8


from itertools import permutations


number = range(1, int(input())+1)

for p in permutations(number):
    print(' '.join(map(str, p)))
