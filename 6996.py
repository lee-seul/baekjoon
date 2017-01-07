# coding: utf-8

n = int(input())

for _ in range(n):
    a, b = input().split()
    a1 = list(a); b1 = list(b)
    if sorted(a1) == sorted(b1):
        print("{} & {} are anagrams.".format(str(a), str(b)))
    else:
        print("{} & {} are NOT anagrams.".format(str(a), str(b)))

