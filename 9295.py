# coding: utf-8

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    print("Case {}: {}".format(i+1, x+y))

