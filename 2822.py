# coding: utf-8

scores = []

for _ in range(8):
    score = int(input())
    scores.append(score)

problem = []
total = 0

for _ in range(5):
    max_num = max(scores)
    for i in range(8):
        if max_num == scores[i]:
            total += scores[i]
            problem.append(i+1)
            scores[i] = 0

problem.sort()

print(total)
for p in problem:
    print(p, end=" ")

