# coding: utf-8


def find_pangram(string):
    alphabet = [chr(x) for x in range(97, 123)]
    
    result = ''
    string = list(set(string))
    for char in alphabet:
        if not char in string:
            result += char
    if result == '':
        result = 'pangram'
    else:
        result = 'missing ' + result
    return result


n = int(input())

for _ in range(n):
    string = input().lower()
    print(find_pangram(string))
