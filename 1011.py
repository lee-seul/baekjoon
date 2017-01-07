# coding: utf-8


def solution(num):
    x = 0
    total = 0
    while num > total:
        x+= 1
        total += 2 * x
    total -= x
    x *= 2
    if num <= total:
        return x - 1
    return x

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    result = solution(y - x)
    print(result)
