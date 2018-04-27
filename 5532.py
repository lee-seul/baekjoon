# coding: utf-8 


import math


vals = []
for _ in range(5):
    num = int(input())
    vals.append(num)

a = math.ceil(vals[1] / vals[3])
b = math.ceil(vals[2] / vals[4])

if a > b:
    l = vals[0] - a
else:
    l = vals[0] - b

print(l)

