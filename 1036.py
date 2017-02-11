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

def sort_list(l, max_length):
    result = []
    for i in range(max_length, -1, -1):
        temp = []
        for e in l:
            if len(e) == i:
                temp.append(e)
        temp.sort()
        if temp:
            result += temp
    return result


n = int(input())
numbers = []
leng = []

for _ in range(n):
    number = list(input())
    numbers.append(number)
    leng.append(len(number))

k = int(input())

numbers = sort_list(numbers, max(leng))

cnt = 0
i = 0
j = 0
while True:
    numbers[i][j] = "Z"
    cnt += 1
    if cnt == k:
        break
    i += 1
    if len(numbers) == i:
        i = 0
        j += 1
        numbers.sort()

result = 0
for i in range(len(numbers)):
    result += c36_to_10("".join(numbers[i]))
    print("".join(numbers[i]))

print(c10_to_36(result))



