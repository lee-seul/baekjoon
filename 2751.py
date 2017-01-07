# coding: utf-8

import sys
write = sys.stdout.write
read = sys.stdin.readline
l = []
n = int(read())
for i in range(n):
    l.append(int(read()))

l.sort()

# 병합 정렬
#def merge_sort(a):
#    if len(a) <= 1: return a
#    half = len(a)//2
#    left = merge_sort(a[:half])
#    right = merge_sort(a[half:])
#    mer = []
#    while len(left) > 0 and len(right) > 0:
#        if left[0] > right[0]:
#            mer.append(right[0])
#            right.pop(0)
#        else:
#            mer.append(left[0])
#            left.pop(0)
#    if len(left) > 0: mer += left
#    if len(right) > 0: mer += right
#    return mer


for i in l:
    write(str(i) + "\n")
