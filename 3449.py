# coding: utf-8

t = int(input())

for _ in range(t):
    a = input()
    b = input()
    result = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            result += 1 
    print("Hamming distance is {}.".format(result))

