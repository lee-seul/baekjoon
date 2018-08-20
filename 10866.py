# coding: utf-8


import sys


def sys_print(value):
    return sys.stdout.write(str(value)+'\n')




n = int(input())

d = []
for _ in range(n):
    statement = sys.stdin.readline().strip()
    statement = statement.split()
    s = statement[0]
    if s == 'push_back':
        d.append(statement[1])

    if s == 'push_front':
        d.insert(0, statement[1])

    if s == 'pop_front':
        if not len(d):
            sys_print(-1)
        else:
            sys_print(d.pop(0))

    if s == 'pop_back':
        if not len(d):
            sys_print(-1)
        else:
            sys_print(d.pop())

    if s == 'size':
        sys_print(len(d))

    if s == 'empty':
        if not len(d):
            sys_print(1)
        else:
            sys_print(0)

    if s == 'front':
        if not len(d):
            sys_print(-1)
        else:
            sys_print(d[0])

    if s == 'back':
        if not len(d):
            sys_print(-1)
        else:
            sys_print(d[-1])


