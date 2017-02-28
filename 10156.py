# coding: utf-8

k, n, m = map(int, input().split())

if k * n > m:
    print(k * n - m)
else:
    print(0)

