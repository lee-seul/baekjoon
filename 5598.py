# coding: utf-8

def decrytion(code):
    result = ""
    for ch in code:
        ch = ord(ch) - 68
        ch %= 26
        ch += 65
        result += chr(ch)
    return result

line = input()
print(decrytion(line))

