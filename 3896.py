# coding: utf-8

def count_sequence(num):
    if num < 2:
        return 0
    pre, nex = 0, 0
    numbers = [0 for _ in range(1299710)]
    for i in range(2, len(numbers)):
        if not numbers[i]:
            n = 2
            if i >= num:
                nex = i
            if i <= num:
                pre = i
            if i >= num:
                break
            while i*n < 1299710:
                numbers[n*i] = 1
                n += 1
    return nex - pre


t = int(input())

for _ in range(t):
    print(count_sequence(int(input())))

