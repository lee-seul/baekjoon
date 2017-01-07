# coding: utf-8

string = input()
l = string.split(" ")
print(len(list(filter(lambda x: x not in " ", l))))



