# coding: utf-8


n = int(input())

sequence = [1, 1, 1]


for i in range(3, n):
    value = sequence[i-1] + sequence[i-3]
    sequence.append(value)

print(sequence[n-1])
