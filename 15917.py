# coding: utf-8


import sys
from math import log


q = int(input())

values = [2 ** x for x in range(31)]
for _ in range(q):
    n = int(sys.stdin.readline())
    if n in values:
        print(1)
    else:
        print(0)
