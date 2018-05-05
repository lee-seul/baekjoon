# coding: utf-8


while True:
    a, b, c = map(int, input().split())
    if not a and not b and not c:
        break
    
    ap1 = b - a
    ap2 = c - b
    if ap1 == ap2:
        print('AP', c + ap1)
        continue

    gp1 = b // a
    gp2 = c // b
    if gp1 == gp2:
        print('GP', c * gp1)

