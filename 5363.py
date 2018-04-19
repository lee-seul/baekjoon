# coding: utf-8


def say_yoda(words):
    result = words[2:]
    result += words[:2]
    return ' '.join(result)

n = int(input())


for _ in range(n):
    string = input().split()
    print(say_yoda(string))
