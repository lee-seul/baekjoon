# coding: utf-8


def find_origin(seq):
    origin = [seq[0]]

    for i in range(1, len(seq)):
        temp = seq[i] * (i + 1)
        temp -= sum(origin)
        origin.append(temp)

    return origin


n = int(input())
numbers = list(map(int, input().split()))

result = find_origin(numbers)
result = map(str, result)

print(" ".join(result))


