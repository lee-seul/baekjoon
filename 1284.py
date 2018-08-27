# coding: utf-8


while True:
    n = input()
    if n == '0':
        break

    length = len(n)
    one = n.count('1')
    zero = n.count('0')
    result = one * 2 + zero * 4 + length + 1
    result += (length - (zero + one)) * 3
    print(result)

