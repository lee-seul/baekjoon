# coding: utf-8


def solution(string, rule):
    result = ''
    for c in string:
        if c == ' ':
            result += c
            continue
        idx = ord(c) - 65
        result += rule[idx]
    return result


t = int(input())

for _ in range(t):
    s = input()
    r = input()

    print(solution(s, r))
