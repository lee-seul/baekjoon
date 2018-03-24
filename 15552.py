# coding-utf-8

import sys

count = sys.stdin.readline().rstrip()
count = int(count)

for _ in range(count):
    numbers = sys.stdin.readline().rstrip().split()
    number = sum(list(map(int, numbers)))
    number = str(number) + '\n'
    
    sys.stdout.write(number)
