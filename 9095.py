# coding: utf-8

def solution(num):
    result = [1, 2, 4]
    if num < 3:
        return result[num-1]
    else:
        for i in range(3, num):
            value = result[i-1] + result[i-2] + result[i-3]
            result.append(value)
        return result[-1]

n = int(input())

for _ in range(n):
    t = int(input())
    print(solution(t))

