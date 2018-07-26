# coding: utf-8

n, t = map(int, input().split())

tasks = list(map(int, input().split()))

cnt = 0
time= 0
for task in tasks:
    if time + task > t:
        break
    
    time += task
    cnt += 1
print(cnt)

