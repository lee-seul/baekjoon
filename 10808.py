# coding: utf-8

s = input()
l = []
for i in range(97, 123):
    l.append(s.count(chr(i)))

for n in l:
    print(n, end=" ")

