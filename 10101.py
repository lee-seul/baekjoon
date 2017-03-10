# coding: utf-8

angles = []
for _ in range(3):
    angle = int(input())
    angles.append(angle)

result = "Error"
if sum(angles) == 180:
    result = "Scalene"
    angles = set(angles)
    if len(angles) == 1:
        result = "Equilateral"
    elif len(angles) == 2:
        result = "Isosceles"

print(result)

