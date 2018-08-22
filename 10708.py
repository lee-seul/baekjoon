# coding: utf-8


n = int(input())
m = int(input())
targets = [int(x) for x in input().split()]
points = [0 for x in range(n)]

for i in range(m):
    numbers = [int(x) for x in input().split()]
    bonus = 0
    for j, num in enumerate(numbers):
        if num == targets[i]:
            points[j] += 1
        
        if not num == targets[i]:
            bonus += 1

    points[targets[i]-1] += bonus
        


for point in points:
    print(point)

