# coding: utf-8


import sys


def fast_input():
    string = sys.stdin.readline().rstrip()
    string = string.split()
    return list(map(int, string))


def get_sum_list(numbers):
    result = [0 for _ in range(len(numbers))]
    for i, number in enumerate(numbers):
        if i == 0:
            result[i] = number
        else:
            result[i] = result[i-1] + number
    return result


n, m = fast_input()
numbers = fast_input()

sum_list = get_sum_list(numbers)

for _ in range(m):
    i, j = fast_input()
    result = sum_list[j-1]
    if i > 1:
        result -= sum_list[i-2]

    print(result)

