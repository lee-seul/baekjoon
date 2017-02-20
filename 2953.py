# coding: utf-8

max_num = 0
num = 0 
for i in range(5):
    scores = list(map(int, input().split()))
    score = sum(scores)
    if max_num < score:
        max_num = score
        num = i + 1

print(num, max_num)

