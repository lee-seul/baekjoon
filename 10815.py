# coding: utf-8

import sys
write = sys.stdout.write
read = sys.stdin.readline

n = int(input())
n_list = list(map(int, read().split()))
m = int(input())
m_list = list(map(int, read().split()))

n_list.sort()
for i in range(len(m_list)):
    start = 0
    end = len(n_list) - 1
    result = "0"
    while start <= end:
        mid = (start + end) // 2
        if m_list[i] < n_list[mid]:
            end = mid - 1
        elif m_list[i] == n_list[mid]:
            result = "1"
            break
        else:
            start = mid + 1
    m_list[i] = result

write(" ".join(m_list))

