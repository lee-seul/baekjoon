# coding: utf-8

n = int(input())

if n == 1:
    print("*")
else:
    for i in range(n*2):
        if not i % 2 and n % 2:
            print("*", end=" ")
        elif i % 2:
            print("", end=" ")
        print("*", end="")
        for j in range(1, n//2):
            print(" *", end="")
        print()

