# coding: utf-8

from math import sqrt


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

a, b = map(int, input().split())

bottom = b - a
top = int(sqrt(b)) - (int(sqrt(a)) + 1) + 1

if top == 0:
    print(0)
else:
    div = gcd(bottom, top)
    print("{}/{}".format(top//div, bottom//div))
