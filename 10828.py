# coding: utf-8

stack = []

def push(n):
    stack.append(n)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

n = int(input())

for i in range(n):
    order = input().split()
    if order[0] == "push":
        push(order[1])
    elif order[0] == "pop":
        pop()
    elif order[0] == "size":
        size()
    elif order[0] == "empty":
        empty()
    elif order[0] == "top":
        top()



