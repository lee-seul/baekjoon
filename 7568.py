# coding: utf-8

n = int(input())

people = []

for _ in range(n):
    value = tuple(map(int, input().split()))
    people.append(value)

rank = 1
result = []
for weight1, height1 in people:
    for weight2, height2 in people:
        if weight1 < weight2 and height1 < height2:
            rank += 1
    result.append(rank)
    rank = 1

for i in result:
    print(i, end=" ")

