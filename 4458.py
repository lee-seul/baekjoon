# coding: utf-8

n = int(input())
string = []

for _ in range(n):
    string.append(input())
    temp = list(string[-1]) 
    temp[0] = temp[0].upper()
    string[-1] = "".join(temp)

for s in string:
    print(s)

