# coding: utf-8


def tower_of_hanoi(n, frompeg, topeg, auxpeg):
    if n == 1:
        print("{} {}".format(frompeg, topeg))
        return
    tower_of_hanoi(n-1, frompeg, auxpeg, topeg)
    print("{} {}".format(frompeg, topeg))
    tower_of_hanoi(n-1, auxpeg, topeg, frompeg)


n = int(input())


cnt = 2**n - 1
print(cnt)

if n <= 20:
    tower_of_hanoi(n, 1, 3, 2)

