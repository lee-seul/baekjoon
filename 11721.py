# coding: utf-8

s = input()

for i in range(len(s)):
    if i != 0 and i % 10 == 0:
        print()
    print(s[i], end="")
