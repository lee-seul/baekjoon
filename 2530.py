# coding: utf-8

A, B, C = map(int, input().split())
D = int(input())

A += D//3600
B += (D%3600) // 60
C += D % 60

if C >= 60:
    B += 1
    C -= 60
if B >= 60:
    A += 1
    B -= 60

print(A%24, B, C)

