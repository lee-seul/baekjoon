# coding: utf-8


def lcm(m, n):
    a = m
    b = n
    while a % b:
        temp = a
        a = b
        b = temp % a
    return (m*n)//b 



t = int(input())

for _ in range(t):
    num1, num2 = map(int, input().split())
    print(lcm(num1, num2))

