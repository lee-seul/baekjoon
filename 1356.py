# coding: utf-8


def multiple(num):
    result = 1
    for n in num:
        result *= int(n)
    return result


def solution(number):
    length = len(number)

    for i in range(1, length):
        left = multiple(number[:i])
        right = multiple(number[i:])
        if left == right:
            print('YES')
            return
    print('NO')


n = input()
solution(n)

