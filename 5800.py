# coding: utf-8

t = int(input())

result = []
for _ in range(t):
    scores = list(map(int, input().split()))
    n = scores[0] 
    scores = scores[1:]
    scores.sort()
    gap = 0
    for i in range(n-1):
        if gap < scores[i+1] - scores[i]:
            gap = scores[i+1] - scores[i]
    result.append([max(scores), min(scores), gap])

for i in range(len(result)):
    print("Class {}\nMax {}, Min {}, Largest gap {}".format(
        i + 1, result[i][0], result[i][1], result[i][2]))

