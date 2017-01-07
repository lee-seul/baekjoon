# coding: utf-8

n = int(input())

def d(n):
    return n + sum(list(map(int, str(n))))

i = 1
while i <= n:
    if n == d(i):
        print(i)
        break
    if n == i:
        print(0)
    i += 1
