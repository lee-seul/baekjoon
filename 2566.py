# coding: utf-8

numbers = []
for _ in range(9):
    numbers.append(list(map(int, input().split())))

m = 0
for i in range(9):
    if m < max(numbers[i]):
        m = max(numbers[i])

x, y = 0, 0
for i in range(9):
    for j in range(9):
        if numbers[i][j] == m:
            x = i + 1
            y = j + 1
            break
print(m)
print(x, y)
