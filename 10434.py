# coding: utf-8

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if not num % i:
            return False
    return True 


def oper(num):
    result = 0
    num = str(num)
    for n in num:
        result += int(n) ** 2
    return result



def is_happy(num):
    if not is_prime(num):
        return 'NO'
    memory = []
    while not num in memory:
        memory.append(num)
        num = oper(num)
        if num == 1:
            return 'YES'
    return 'NO'


p = int(input())

for _ in range(p):
    i, n = map(int, input().split())
    result = is_happy(n)
    print(i, n, result)
