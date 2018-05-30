# coding: utf-8 


def sum_digit(num):
    num = str(num)
    return int(num[0]) + int(num[1])


def check_credit_card(numbers):
    numbers = list(numbers)
    numbers = list(map(int, numbers))
    numbers.reverse()
    for i, number in enumerate(numbers):
        if not i % 2:
            continue
        number *= 2
        if number >= 10:
            numbers[i] = sum_digit(number)
        else:
            numbers[i] = number
    return sum(numbers) 


t = int(input())

for _ in range(t):
    s = input()
    result = check_credit_card(s)
    if result % 10:
        print('F')
    else:
        print('T')
