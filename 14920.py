# coding: utf-8


def cn(c):
    if not c % 2:
        return c // 2
    return 3 * c + 1


c = int(input())

n = 1
while True:
    if c == 1:
        print(n)
        break
    c = cn(c)
    n += 1

