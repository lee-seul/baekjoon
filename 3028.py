# coding: utf-8

def change(x, y):
    return [y, x]

A, B, C = 1, 0, 0

order = input()

for o in order:
    if o == "A":
        A, B = change(A, B)
    elif o == "B":
        B, C = change(B, C)
    elif o == "C":
        A, C = change(A, C)

if A:
    print(1)
elif B:
    print(2)
elif C:
    print(3)

