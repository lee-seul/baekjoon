# coding: utf-8

n = int(input())
v =input()

a = v.count("A")
b = v.count("B")

if a > b:
    print("A")
elif a == b:
    print("Tie")
else:
    print("B")


