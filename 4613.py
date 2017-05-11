# coding: utf-8


def quicksum(string):
    result = 0
    for i, c in enumerate(string):
        temp = ord(c) - 64
        if c == ' ':
            temp = 0
        result += temp * (i + 1)
    return result
        


while True:
    s = input()
    if s == '#':
        break
    result = quicksum(s)
    print(result)

