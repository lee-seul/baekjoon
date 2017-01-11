# coding: utf-8

n = int(input())
star = "* " * n

for i in range(n):
    if i % 2 == 0:
        print(star)
    else:
        print(" " + star)
