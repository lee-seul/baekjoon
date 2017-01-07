# coding: utf-8

n = int(input())
l = ["S", "R", "P"]

for _ in range(n):
    cnt = int(input())
    p1 = 0
    p2 = 0
    for _ in range(cnt):
        player1, player2 = input().split()
        if (l.index(player1)+1)%3 ==  l.index(player2):
            p2 += 1
        elif (l.index(player2)+1)%3 == l.index(player1):
            p1 += 1
        print(p1, p2)
    if p1>p2:
        print("Player 1")
    elif p1==p2:
        print("TIE")
    else:
        print("Player 2")

