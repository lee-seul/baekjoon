# coding: utf-8

import sys

read = sys.stdin.readline


def selection_sort(l):
    for i in range(1, len(l)):
        temp = l[i]
        for j in range(i-1, -1, -1):
            if l[j] > temp:
                l[j+1] = l[j]
            else:
                l[j+1] = temp
                break
    return l


n, k = map(int, input().split())

seq = [0 for i in range(n+1)]

for i in range(n):
    seq[i] = int(read())

seq = selection_sort(seq)
start = (k+1)//2
end = start + n-k+1

print(sum(seq[start:end]))

