# coding: utf-8


def count_char(char, string): 
    string = ''.join(string)
    string = string.lower()
    print(char, string.count(char))


while True:
    string = input()
    if string == '#':
        break 
    char, *string = string.split()
    count_char(char, string)    

