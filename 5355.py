# coding: utf-8

t = int(input())

for _ in range(t):
    s = input().split()
    result = float(s[0])
    for i in range(1, len(s)):
        if s[i] == '@':
            result *= 3
        elif s[i] == '%':
            result += 5
        elif s[i] == '#':
            result -=7
    print("{:.2f}".format(result))

