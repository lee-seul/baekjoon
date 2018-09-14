# coding: utf-8


def e(a, b, x):
    return (a*x+b) % 26


d = {chr(x+65): x for x in range(26)} 


t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    string = input()
    result = ''
    for char in string:
        temp = e(a, b, d[char])
        result += chr(temp+65)

    print(result)
