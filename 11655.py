# coding: utf-8


def rot13(string):
    result = ''
    large = [chr(x) for x in range(65, 91)] 
    small = [chr(x) for x in range(97, 123)] 
    
    for char in string:
        if char in large or char in small:
            idx = ord(char) + 13
            if char in large and idx > 90:
                idx -= 26

            if char in small and idx > 122:
                idx -= 26

            char = chr(idx)
        result += char
    return result



s = input()
print(rot13(s))
