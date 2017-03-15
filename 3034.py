# coding: utf-8

n, w, h = map(int, input().split())

d = w ** 2 + h ** 2

for _ in range(n):
    a = int(input())
    if a*a <= d:
        print("DA")
    else:
        print("NE")

