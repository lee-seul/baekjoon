# coding: utf-8


import sys


numbers = sys.stdin.readline().strip()
numbers = numbers.split()

count = 0
for idx, number in enumerate(numbers):
    if int(number) > 0:
        count += 1

print(count)

