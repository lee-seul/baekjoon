# coding: utf-8


def cal(a, b):
    return (a+b) * (a-b)

a, b = map(int, input().split())
print(cal(a, b))
