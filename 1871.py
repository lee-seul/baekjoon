# coding: utf-8


def string_to_value(string):
    result = 0
    string = list(string)
    string.reverse()
    for i, c in enumerate(string):
        temp = ord(c) - 65
        result += temp * (26**i)
    return result

n = int(input())

for _ in range(n):
    number = input()
    front = number[:3]
    rear = int(number[4:])
    front = string_to_value(front)
    value = front - rear
    if abs(value) <= 100:
        print("nice")
    else:
        print("not nice")

