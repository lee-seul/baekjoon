# coding: utf-8

space = [[0 for j in range(101)] for i in range(101)]

values = []
for _ in range(4):
    l = list(map(int, input().split()))
    values.append(l)

for value in values:
    for i in range(value[0], value[2]):
        for j in range(value[1], value[3]):
            space[i][j] = 1

result = 0
for i in range(101):
    result += space[i].count(1)

print(result)


