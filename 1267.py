# coding: utf-8


def calculate_y(time):
    y = time // 30 + 1
    return y * 10 


def calculate_m(time):
    m = time // 60 + 1
    return m * 15 


n = int(input())

times = list(map(int, input().split()))

y = sum(list(map(calculate_y, times)))
m = sum(list(map(calculate_m, times)))

if y > m:
    print('M', m)
elif y < m:
    print('Y', y)
else:
    print('Y M', m)

