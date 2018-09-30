# coding: utf-8


t = int(input())
for _ in range(t):
    k = int(input())
    students = [int(x) for x in input().split()]
    n = int(input())
    su = []
    for _ in range(n):
        num, hour, minute = map(int, input().split())
        if hour == -1:
            continue
        time = hour * 60 + minute
        if num in students and time <= 360:
            su.append((num, time))

    su = sorted(su, key=lambda x: x[1])
    print(su[0][0], len(su))
                
                
