# coding: utf-8

scores = []
for _ in range(6):
    score = int(input())
    scores.append(score)

result = max(scores[4:])
scores = scores[:4]
scores.sort()
result += sum(scores[1:])

print(result)

