# coding: utf-8

t = int(input())

for _ in range(t):
    scores = list(map(int, input().split()))
    scores.sort()
    scores = scores[1:4]
    if scores[2] - scores[0] >= 4:
        print("KIN")
    else:
        print(sum(scores))

