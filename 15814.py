# coding: utf-8


def change_position(string, a, b):
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    return string


s = list(input())
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    s = change_position(s, a, b)

print(''.join(s))

