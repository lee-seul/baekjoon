# coding: utf-8


t = int(input())


for _ in range(t):
    s = input().split()
    ignore = []
    while True:
        string = input()
        if 'fox' in string:
            break

        string = string.split()[-1]
        ignore.append(string)

    result = []
    for char in s:
        if not char in ignore:
            result.append(char)

    print(' '.join(result))
