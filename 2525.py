# coding: utf-8

A, B = map(int, input().split())
C = int(input())

A += C // 60
B += C % 60

if B >= 60:
    A += 1
    B -= 60

print(A % 24, B % 60)

