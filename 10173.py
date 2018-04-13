# coding: utf-8


while True:
    string = input()
    if string == 'EOI':
        break
    string = string.lower()
    if 'nemo' in string:
        print('Found')
    else:
        print('Missing')

