# coding: utf-8


l = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]


def sum_name(a, b):
    result = ''
    length = len(a)
    for i in range(length):
        result += a[i]
        result += b[i]
    return result


def name_to_num(name):
    result = []
    for char in name:
        idx = ord(char) - 65
        result.append(l[idx])
    return result


def solution(numbers):
    while True:
        length = len(numbers)
        if length == 2:
            return numbers        
    
        result = []
        for i in range(length-1):
            temp = numbers[i] + numbers[i+1]
            temp %= 10
            result.append(temp)
        numbers = result

A = input()
B = input()

name = sum_name(A, B)
numbers = name_to_num(name)

ans = solution(numbers)

print('{}{}'.format(ans[0], ans[1]))

