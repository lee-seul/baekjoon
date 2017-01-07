# coding: utf-8


def find(l, c):
    for i in range(len(l)):
        if c in l[i]:
            return i

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXZY']

string = input()
result = 0
for i in range(len(string)):
    result += find(dial, string[i]) + 3

print(result)
