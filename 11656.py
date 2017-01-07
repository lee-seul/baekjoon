# coding: utf-8

s = input()
leng = len(s)
l = []
for i in range(leng):
    l.append(s[i:])
l.sort()

for c in l:
    print(c)

