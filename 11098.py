# coding: utf-8


t = int(input())

for _ in range(t):
    players = []
    p = int(input())
    for _ in range(p):
        player = input().split()
        player[0] = int(player[0])
        players.append(player)
    players.sort()
    print(players[-1][1])
        

