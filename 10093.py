# coding: utf-8


import sys


def solution(a, b):
    print(b-a-1)
    for i in range(a+1, b):
        num = str(i)
        if i != b-1:
            num += ' '
        sys.stdout.write(num)


a, b = map(int, input().split())

if a == b:
    print(0)
if a > b:
    solution(b, a)
if a < b:
    solution(a, b)



