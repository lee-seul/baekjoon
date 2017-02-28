# coding: utf-8

t = int(input())

for _ in range(t):
    yon = 0
    kor = 0
    for _ in range(9):
        y, k = map(int, input().split())
        yon += y
        kor += k
    if yon > kor:
        print("Yonsei")
    elif yon == kor:
        print("Draw")
    else:
        print("Korea")

