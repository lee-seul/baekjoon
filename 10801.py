# coding: utf-8

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = 0
b = 0
for i in range(10):
    if A[i] > B[i]:
        a += 1
    elif A[i] < B[i]:
        b += 1

if a > b:
    print("A")
elif a == b:
    print("D")
else:
    print("B")


