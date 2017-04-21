# coding: utf-8

import sys

read = sys.stdin.readline


def selection_sort(l):
    for i in range(len(l)-1):
        idx = i
        for j in range(i+1, len(l)):
            if l[j] < l[idx]:
                idx = j
        temp = l[idx]
        l[idx] = l[i]
        l[i] = temp
    return l


n, k = map(int, input().split())

seq = [0 for i in range(n+1)]

for i in range(n):
    seq[i] = int(read())

result = 0
idx = (k+1)//2 - 1

for i in range(k, n+1):
    sub_seq = seq[i-k:i]
    sub_seq = selection_sort(sub_seq)
    result += sub_seq[idx]


print(result)
