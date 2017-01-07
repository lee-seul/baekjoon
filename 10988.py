# coding: utf-8


def is_palindrom(string):
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)]:
            return 0
    return 1

s = input()

print(is_palindrom(s))


