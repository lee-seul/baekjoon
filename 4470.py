# coding: utf-8

n = int(input())
string = []
for _ in range(n):
    string.append(input())

for i in range(n):
    print("{}. {}".format(i+1, string[i]))

