# coding: utf-8

a = int(input())
b = int(input())

num = list(str(b))
num.reverse()
for c in num:
    print(a*int(c))
print(a*b)
