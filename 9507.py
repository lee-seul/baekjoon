# coding: utf-8

def fibo(num):
    if num < 2:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        l = [1, 1, 2, 4]
        for i in range(4, num+1):
            value = l[i-1] + l[i-2] + l[i-3] + l[i-4]
            l.append(value)
        return l[-1]

t = int(input())

for _ in range(t):
    result = fibo(int(input()))
    print(result)

