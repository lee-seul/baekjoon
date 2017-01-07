# coding: utf-8

x, y = map(int, input().split())

def rev(n):
    l = list(str(n))
    l.reverse()
    return int("".join(l))

print(rev(rev(x) + rev(y)))

