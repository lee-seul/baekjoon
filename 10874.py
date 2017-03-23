# coding: utf-8

ans = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

n = int(input())

result = []
for i in range(n):
    exam = list(map(int, input().split()))
    if ans == exam:
        result.append(i+1)

for r in result:
    print(r)
