# coding: utf-8

import sys
string = sys.stdin.readlines(64)

result = 0
for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0 and string[i][j] == 'F':
                result += 1
        else:
            if j % 2 == 1 and string[i][j] == 'F':
                result += 1

print(result)


