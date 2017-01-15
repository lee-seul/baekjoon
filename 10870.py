# coding: utf-8

n = int(input())
a = 0
b = 1

for i in range(n):
    tmp = b
    b = a + b
    a = tmp

print(a)
