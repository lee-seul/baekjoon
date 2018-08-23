# coding: utf-8


def count_integer(n, m):
    result = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            value = (i*i+j*j+m)%(i*j)
            if not value:
                result += 1
    return result


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(count_integer(n, m))

