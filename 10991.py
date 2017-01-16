# coding: utf-8

n = int(input())
star = "* "
blank = " "

for i in range(1, n+1):
    print(blank*(n-i) + star * i)
