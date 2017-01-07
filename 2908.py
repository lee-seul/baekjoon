# coding: utf-8

a, b = input().split()
a = list(a)
b = list(b)
a.reverse()
b.reverse()
a = "".join(a)
b = "".join(b)
if a > b:
    print(a)
else:
    print(b)

