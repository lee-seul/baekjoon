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
        while n * v <= num:
            n += 1
        result += l[n-1]
        c = v * (n-1)
        num -= c
    return result

def solution(li, max_length ,count):
    l = []
    for e in li:
        l.append(list(e))
    result = []
    while max_length > 0 and len(result) < count:
        temp = []
        for e in l:
            if len(e) == max_length: 
                if e[0] not in result and e[0] not in temp:
                    temp.append(e.pop(0))
                else:
                    e.pop(0)
        temp.sort()
        result += temp
        max_length -= 1
    return result[:count]
    

n = int(input())
numbers = []
leng = []

for _ in range(n):
    number = input()
    numbers.append(number)
    leng.append(len(number))

k = int(input())

selected_numbers = solution(numbers, max(leng), k)
result = 0

for num_36 in numbers:
    for sel in selected_numbers:
        num_36 = num_36.replace(sel, "Z")
    result += c36_to_10(num_36)

print(c10_to_36(result))

