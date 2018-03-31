# coding: utf-8


point = {chr(x+64):x for x in range(1, 27)}


def get_point(life):
    result = 0
    for char in life:
        if char in point.keys():
            result += point[char]

    if result == 100:
        result = 'PERFECT LIFE'
    return result


n = int(input())

for _ in range(n):
    life = input()
    print(get_point(life))

