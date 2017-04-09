# coding: utf-8


n = int(input())
dots = []

for _ in range(n):
    dot = list(map(int, input().split()))
    dot = tuple([dot[1], dot[0]])
    dots.append(dot)

dots.sort()

for dot in dots:
    print(dot[1], dot[0])

