# coding: utf-8


def round_num(num):
    length = len(num)
    num = int(num)
    if length == 1:
        return num
    for i in range(length):
        print(num, i)
        num = round(num, -i)
    return num


n = int(input())


for _ in range(n):
    num = input()
    print(round_num(num))
