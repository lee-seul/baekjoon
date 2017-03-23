# coding: utf-8

from math import log

def is_two_power(num):
    if 2**int(log(num, 2)) == num:
        return 1
    return 0

n = int(input())
print(is_two_power(n))

