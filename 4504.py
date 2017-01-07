# coding: utf-8

n = int(input())
l = []
while True:
    a = int(input())
    if a == 0:
        break
    l.append(a)

for i in l:
    if i % n == 0:
        print("{} is a multiple of {}.".format(i, n))
    else:
        print("{} is NOT a multiple of {}.".format(i, n))
