# coding: utf-8


def find_pangram(string):
    alphabet = [chr(x) for x in range(97, 123)]
    
    result = ''
    string = list(set(string))
    for char in alphabet:
        if not char in string:
            result += char
    if result == '':
        result = 'Y'
    else:
        result = 'N'
    return result


while True:
    string = input()
    if string == '*':
        break 
    print(find_pangram(string))
