# coding: utf-8

n = int(input())
s = n - 1

star = "*"
space = " "

print(space * s + "*")
for i in range(2, n+1):
    s -= 1
    string = s * space + star + space * (1 + (i-2)*2) + star
    print(string)
