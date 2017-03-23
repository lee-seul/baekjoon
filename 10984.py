# coding: utf-8

t = int(input())

for _ in range(t):
    n = int(input())
    score = 0
    total = 0
    for _ in range(n):
        s, t = map(float, input().split())
        score += s
        total += s * t
    print("{} {:.1f}".format(int(score), total/score))

