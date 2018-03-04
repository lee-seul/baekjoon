# coding: utf-8


def to_num(bi):
    length = len(bi) - 1
    result = 0
    for i, b in enumerate(bi):
        if b == '0':
            continue
        if b == '1':
            result += 2 ** (length - i)
    return result


bis = sum(list(map(to_num, input().split())))

print(bin(bis)[2:])

