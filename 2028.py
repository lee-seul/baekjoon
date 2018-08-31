# coding: utf-8


def ans(num):
    length = -len(num)
    last = str(int(num) ** 2)[length:]
    return last == num


t = int(input())

for _ in range(t):
    n = input()
    if ans(n):
        print('YES')
    else:
        print('NO')

