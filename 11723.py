# coding: utf-8 


import sys


m = int(input())

numbers = set()
for _ in range(m):
    direction = sys.stdin.readline().strip()
    direction = direction.split()
    s = direction[0]
    if len(direction) == 2:
        num = int(direction[1])

    if 'add' == s:
        numbers.add(num)

    elif 'check' == s:
        if num in numbers:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')

    elif 'remove' == s:
        numbers.discard(num)

    elif 'toggle' == s:
        if num in numbers:
            numbers.discard(num)
        else:
            numbers.add(num)

    elif 'all' == s:
        numbers = set(range(1, 21))

    elif 'empty' in direction:
        numbers = set()
