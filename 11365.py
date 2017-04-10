# coding: utf-8


while True:
    code = input()
    if code == 'END':
        break

    code = list(code)
    code.reverse()
    print("".join(code))

