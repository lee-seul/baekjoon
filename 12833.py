# coding: utf-8

a, b, c = map(int, input().split())

if not c % 2:
    print(a)
else:
    print(a^b)


