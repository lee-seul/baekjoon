# coding: utf-8


def rotate(l):
    result = [0] * 4
    order = [2, 0, 3, 1]
    for i in range(4):
        idx = order[i]
        result[i] = l[idx]
    return result


numbers = []

for _ in range(2):
    a, b = map(int, input().split())
    numbers.append(a)
    numbers.append(b)

values = []

for _ in range(4):
    value = numbers[0]/numbers[2] + numbers[1]/numbers[3]
    values.append(value)
    numbers = rotate(numbers)

max_value = max(values)

for i in range(4):
    if max_value == values[i]:
        print(i)
        break


