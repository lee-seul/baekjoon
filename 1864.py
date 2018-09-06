# coding: utf-8


def ox(string):
    char = {
        '-': 0, '\\': 1, '(': 2, '@': 3, '?': 4,
        '>': 5, '&': 6, '%': 7, '/': -1
    }
    result = 0
    length = len(string) - 1
    for i, s in enumerate(string):
        temp = 8 ** (length - i)
        result += char[s] * temp 
    return result



while True:
    o = input()
    if o == '#':
        break
    print(ox(o)) 
