# coding: utf-8

import sys
read = sys.stdin.readline

n, k = map(int, input().split())

scores = []

for _ in range(n):
    score = float(read()) * 10
    scores.append(score)

scores.sort()

scores = scores[k:n-k]


result_1 = sum(scores) / (n - 2 * k)
result_1 /= 10

result_2 = sum(scores) + scores[0] * k + scores[-1] * k
result_2 /= n * 10

print("{:.2f}\n{:.2f}".format(result_1 + 0.00000001, result_2 + 0.00000001))

