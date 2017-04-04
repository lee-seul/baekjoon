# coding: utf-8


result = int(input())
while True:
    s = input()
    if s == '=':
        break
    elif s == '+':
        n = int(input())
        result += n
    elif s == '-':
        n = int(input())
        result -= n
    elif s == '*':
        n = int(input())
        result *= n
    elif s == '/':
        n = int(input())
        result //= n

print(result)

