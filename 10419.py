# coding: utf-8

time = [i**2 + i for i in range(1, 101)] 

T = int(input())

for _ in range(T):
    t = int(input())
    for i in range(100):
        if t < time[i]:
            print(i)
            break

