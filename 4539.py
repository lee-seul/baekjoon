# coding: utf-8


def round_num(num):
    length = len(num)
    if length == 1:
        return int(num)
    for i in range(1, length):
        if int(num[-i]) == 5:
            num = str(int(num) + 10 ** (i-1)) 
        num = round(int(num), -i)
        num = str(num)
    return num


n = int(input())


for _ in range(n):
    num = input()
    print(round_num(num))
