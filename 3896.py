# coding: utf-8

def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            return False
    return True

def count_sequence(num):
    if num < 2 or is_prime(num):
        return 0
    pre, nex = 0, 0
    i = 1
    while True:
        if not pre and is_prime(num-i):
            pre = num - i
        if not nex and is_prime(num+i):
            nex = num + i
        if pre and nex:
            break
        i += 1
    return nex - pre


t = int(input())

for _ in range(t):
    print(count_sequence(int(input())))

