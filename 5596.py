# coding: utf-8

s = sum(list(map(int, input().split())))
t = sum(list(map(int, input().split())))

if s >= t:
    print(s)
else:
    print(t)

