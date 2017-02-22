# coding: utf-8

def count_rec(num):
    result = num
    i = 2
    while i*i <= num:
        j = i
        while j*i <= num:
            result += 1
            j += 1
        i += 1
    return result

n = int(input())

print(count_rec(n))

