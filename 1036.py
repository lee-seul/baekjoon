# coding: utf-8

from math import log

l = [str(x) for x in range(10)]
l += [chr(x) for x in range(65, 91)]

values = {l[x]:x for x in range(36)}


def c36_to_10(num):
    num = list(num)
    num.reverse()
    result = 0
    for i in range(len(num)):
        result += values[num[i]] * (36 ** i)
    return result

def c10_to_36(num):
    length = int(log(num, 36))
    digit = 0
    result = ""
    for i in range(length, -1, -1):
        n = 1
        v = 36 ** i
        while n * v < num:
            n += 1
        result += l[n-1]
        num -= v * (n-1)
    return result

def solution(l, max_length, loop):
    result = 0
    temp = []
    cnt = 0
    not_finish = True
    while not_finish:
        for e in l:
            if len(e) == max_length:
                temp.append(e.pop(0))
        temp.sort()
        for i in range(len(temp)):
            result += 35 * (36 ** (max_length - 1))
            cnt += 1
            if cnt == loop:
                not_finish = False
                if temp:
                    for a in temp:
                        result += values[a] * (36 ** (max_length - 1))
                break
        max_length -= 1
    
    for e in l:
        result += c36_to_10("".join(e))
    return c10_to_36(result) 

n = int(input())
numbers = []
leng = []

for _ in range(n):
    number = list(input())
    numbers.append(number)
    leng.append(len(number))

k = int(input())

print(solution(numbers, max(leng), k))

