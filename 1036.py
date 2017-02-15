# coding: utf-8

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
    temp = []
    while num:
        temp.append(num % 36)
        num //= 36
    
    temp.reverse()
    result = ""
    for i in temp:
        result += l[i]
    return result


n = int(input())
numbers = []

for _ in range(n):
    number = input()
    numbers.append(number)

plus = []
result = 0

k = int(input())

for number in numbers:
    result += c36_to_10(number)

for e in l:
    temp = 0
    for number in numbers:
        num = number.replace(e, "Z")
        temp += c36_to_10(num)
    plus.append(temp - result)

plus.sort()
plus.reverse()

result = c10_to_36(result + sum(plus[:k]))
print(result)

