# coding: utf-8

n = int(input())

students = list(map(int, input().split()))

result = []

for i in range(n):
    result.append(i+1)
    for j in range(students[i]):
        temp = result[i-j]
        result[i-j] = result[i-(j+1)]
        result[i-(j+1)] = temp

for a in result:
    print(a, end=" ")

