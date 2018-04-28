# coding: utf-8


def to_ctp(chars):
    result = []
    for char in chars:
        temp = ord(char) - 64
        result.append(str(temp))
    return ' '.join(result)


def from_ctp(numbers):
    result = []
    for number in numbers:
        temp = int(number) + 64
        result.append(chr(temp))
    return ' '.join(result)


t = int(input())

for _ in range(t):
    n, types = input().split()
    string = input().split()
    if types == 'C':
        print(to_ctp(string))
    else:
        print(from_ctp(string))
