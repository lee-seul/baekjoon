# coding: utf-8


import re


def sum_only_nums(string):
    string = re.sub('[A-Z]', '', string)
    return sum([int(x) for x in list(string)])


n = int(input())
numbers = []
for _ in range(n):
    s = input()
    temp = (len(s), sum_only_nums(s), s)
    numbers.append(temp)

numbers.sort()
for number in numbers:
    print(number[2])

