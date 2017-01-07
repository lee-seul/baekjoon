# coding: utf-8

import sys

n = int(input())
num = sys.stdin.readline()
num = list(map(int, num.split()))

print(len(num))
print(sum(num))

