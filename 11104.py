# coding: utf-8


def make_decimal(binary):
    result = 0
    init = 23
    for bit in binary:
        temp = int(bit) * (2 ** init)
        result += temp
        init -= 1
    return result


t = int(input())

for _ in range(t):
    digit = input()
    print(make_decimal(digit))

