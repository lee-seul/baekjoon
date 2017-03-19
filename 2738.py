# coding: utf-8

n, m = map(int, input().split())
A = []
B = []

for i in range(n*2):
    value = list(map(int, input().split()))
    if i < n:
        A.append(value)
    else:
        B.append(value)

for i in range(n):
    for j in range(m):
        A[i][j] += B[i][j]

for i in range(n):
    for j in range(m):
        print(A[i][j], end=" ")
    print()

