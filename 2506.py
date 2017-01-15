# coding: utf-8

n = int(input())
total = 0
scores = list(map(int, input().split()))

point = 1
for score in scores:
    if score:
        total += point
        point += 1
    else:
        point = 1

print(total)
