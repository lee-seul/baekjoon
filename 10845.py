# coding: utf-8

q = []

def push(x):
    q.append(x)

def empty():
    if len(q) == 0:
        return 1
    return 0

def pop():
    if len(q) == 0:
        return -1
    return q.pop(0)

def size():
    return len(q)

def front():
    if empty() == 0:
        return q[0]
    return -1

def back():
    if empty() == 0:
        return q[-1]
    return -1


n = int(input())

for _ in range(n):
    m = input().split()
    if m[0] == "push":
        push(m[1])
    elif m[0] == 'front':
        print(front())
    elif m[0] == 'back':
        print(back())
    elif m[0] == 'size':
        print(size())
    elif m[0] == 'empty':
        print(empty())
    elif m[0] == 'pop':
        print(pop())
