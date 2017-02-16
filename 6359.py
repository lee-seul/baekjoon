# coding: utf-8

def solution(num):
    l = [0] * (num + 1)
    for i in range(1, num + 1):
        n = 1
        while i * n <= num:
            if l[i*n]:
                l[i*n] = 0
            else:
                l[i*n] = 1
            n += 1
    return l.count(1)


t = int(input())

for _ in range(t):
    result = solution(int(input()))
    print(result)

