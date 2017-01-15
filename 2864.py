# coding: utf-8

a, b = input().split()

a = a.replace("6", "5")
b = b.replace("6", "5")
min_val = int(a) + int(b)

a = a.replace("5", "6")
b = b.replace("5", "6")

print(min_val, int(a) + int(b))
