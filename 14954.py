# coding: utf-8


def function(number):
    result = 0
    for num in number:
        result += int(num) ** 2
    return result


def is_happy(num):
    origin = int(num)
    temp = []
    while True:
        num = function(str(num))
        if num == 1:
            print('HAPPY')
            return 
        if num in temp:
            print('UNHAPPY')
            return 
        temp.append(num)


n = input()
is_happy(n)

