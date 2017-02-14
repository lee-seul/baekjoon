# coding: utf-8


def new_mul(num1, num2):
    num1 = list(map(int, num1))
    num2 = list(map(int, num2))
    result = 0
    for n1 in num1:
        for n2 in num2:
            result += n1 * n2
    return result


a, b = input().split()

print(new_mul(a, b))
