# coding: utf-8

n = int(input())
score = list(map(int, input().split()))

m = max(score)
for i in range(n):
    score[i] = score[i]/m * 100

print("{:.2f}".format(sum(score)/n))

