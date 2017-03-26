# coding: utf-8

t = int(input())

for _ in range(t):
    s = input()
    length = len(s) // 2
    if s[length] == s[length-1]:
        print("Do-it")
    else:
        print("Do-it-Not")


