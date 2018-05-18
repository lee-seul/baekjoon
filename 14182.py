# coding: utf-8


while True:
    n = int(input())
    if not n:
        break
    if n <= 1000000:
        print(n)
    elif n <= 5000000:
        print(int(n*9/10))
    else:
        print(int(n*8/10))
