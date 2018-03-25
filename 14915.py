# coding: utf-8

from math import log


def get_max_digit(m, n):
    return int(log(m, n))


def max_digit(m, n):
    digits = get_max_digit(m, n)

    result = list(range(digits + 1))
    result.reverse()
    return result


def solution(m, digits):
    numbers = {x:chr(55+n) for x in range(10, 16)}

    result = ''
    for digit in digits:
        divide = n ** digit
        if m >= divide:
            mod = m // divide
            m -= divide * mod 
            if mod >= 10:
                result += numbers[mod]
            else:
                result += str(mod)

        else:
            result += '0'

        if m == 0:
            if digit >= 0:
                temp = '0' * digit
                result += temp
            break

    return result


def get_solution(m, n):
    if m == 0:
        print('0')
        return

    digits = max_digit(m, n)

    result = solution(m, digits)
    print (result)


m, n = list(map(int, input().split()))

get_solution(m, n)

