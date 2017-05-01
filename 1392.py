# coding: utf-8


n, q = map(int, input().split())


running = []

for i in range(n):
    t = int(input())
    for _ in range(t):
        running.append(i+1)

for _ in range(q):
    time = int(input())
    print(running[time])

