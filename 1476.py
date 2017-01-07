# coding: utf-8

e, s, m = map(int, input().split())

i = 1
while True:
    a = i % 15; b = i % 28; c = i % 19
    if a == 0:
        a = 15
    if b == 0:
        b = 28
    if c == 0:
        c = 19
    if a == e and b == s and c == m:
        print(i)
        break
    i += 1
