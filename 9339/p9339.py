# coding: utf-8


def solution():
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
    return su[0][0], len(su)
                

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = solution()
        print(a, b)

