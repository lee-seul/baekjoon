# coding: utf-8

l = list(map(int, input().split()))

for i in range(2):
    if l[i] != 1: 
        l[i] = 1 - l[i]
    else: 
        l[i] = 0
for i in range(2, 5):
    if l[i] != 2:
        l[i] = 2 - l[i]
    else:
        l[i] = 0
if l[5] != 8:
    l[5] = 8 - l[5]
else:
    l[5] = 0

for i in l:
    print(i, end=" ")


