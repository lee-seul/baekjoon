# coding: utf-8


n, m, k = map(int, input().split())

row = k // m
col = k % m

print(row, col)

