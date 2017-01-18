# coding: utf-8

m, n = map(int, input().split())
array = []

for _ in range(m):
    array.append(list(map(int, input().split())))

k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    result = 0
    for a in range(i-1, x):
        result += sum(array[a][j-1:y])
    print(result)
