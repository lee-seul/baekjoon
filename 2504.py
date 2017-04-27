# coding: utf-8


while True:
    a, b, c, d = map(int, input().split())
    if not (a and b and c and d):
        break

    print(c-b, d-a)

