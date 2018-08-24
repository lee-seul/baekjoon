# coding: utf-8


def to_int(bin_value):
    result = 0
    bin_value = reversed(list(bin_value))
    for i, digit in enumerate(bin_value):
        if int(digit):
            result += 2 ** i
    return result 


value = input()
num = to_int(value) * 17
print(bin(num)[2:])
