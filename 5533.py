# coding: utf-8

n = int(input())

players = [[0 for _ in range(3)] for _ in range(n)]

numbers = [[0 for _ in range(n)] for _ in range(3)]

for i in range(n):
    player = list(map(int, input().split()))
    for j in range(3):
        players[i][j] = player[j]
        numbers[j][i] = player[j]

for x in range(n):
    temp = numbers
    for y in range(3):
        for z in range(n):
            if x == z:
                continue
            if players[x][y] == numbers[y][z]:
                players[x][y] = 0


for a in range(n):
    print(sum(players[a]))

