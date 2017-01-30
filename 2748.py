# coding: utf-8

def fib(num):
    pre = 0
    cur = 1
    if num < 1:
        return pre
    if num < 2:
        return cur
    for i in range(num-1):
        tmp = pre
        pre = cur
        cur = pre + tmp
    return cur

print(fib(int(input())))
