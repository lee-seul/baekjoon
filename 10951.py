# coding: utf-8

import sys


while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    a, b = map(int, line.split())
    print(a+b)

