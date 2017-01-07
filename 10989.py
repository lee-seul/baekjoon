# coding: utf-8

import sys
write = sys.stdout.write
read = sys.stdin.readline

# 카운팅 소트
l = [0 for i in range(10001)]
n = int(read())

for i in range(n):
    l[int(read())] += 1

for index in range(1, 10001):
    write((str(index)+"\n") * l[index])
