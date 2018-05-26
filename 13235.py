# coding: utf-8


def is_palindromes(string):
    length = len(string) // 2

    for i in range(length):
        if string[i] != string[-(i+1)]:
            return 'false'
    return 'true'


s = input()

print(is_palindromes(s))
