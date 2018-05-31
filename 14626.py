# coding: utf-8


def number_position(isbn):
    idx = isbn.find('*')
    if idx % 2:
        return 3
    return 1


def find_number(number):
    value = 0
    for i, e in enumerate(number):
        if e == '*':
            continue

        temp = int(e)
        if i % 2:
            temp *= 3
        value += temp
    return value 





isbn = input()

value = find_number(isbn)
num = number_position(isbn)

for i in range(10):
    if not (value + (i * num)) % 10:
        print(i)


