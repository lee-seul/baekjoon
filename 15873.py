# coding: utf-8


ab = input()

if len(ab) == 2:
    print(int(ab[0]) + int(ab[1]))
if len(ab) == 3:
    if ab[1] == '0':
        print(int(ab[:2]) + int(ab[2]))
    else:
        print(int(ab[0]) + int(ab[1:]))
if len(ab) == 4:
    print(int(ab[:2]) + int(ab[2:]))
