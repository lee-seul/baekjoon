# coding: utf-8


def sum_digit(number):
    result = 0
    for n in number:
        result += int(n)
    return str(result)


def make_len_1(number):
    while True:
        if len(number) == 1:
            return number
        number = str(sum_digit(number))


while True:
    n = input()
    if n == '0':
        break 
    print(make_len_1(n))
