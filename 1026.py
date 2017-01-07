# coding: utf-8

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
A.reverse()
B.sort()

S = 0
for i in range(n):
    S += A[i] * B[i]

print(S)

