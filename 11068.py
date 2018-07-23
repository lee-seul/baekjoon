# coding: utf-8


def is_true(num):
    length = len(num) // 2
    for i in range(length):
        if not num[i] == num[-i-1]:
            return False
    return True


def convert(n, base):
    result = []

    while True:
        q, r = divmod(n, base)
        result.append(r)
        if q == 0:
            break
        
        n = q
    return result

        

    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]



n = int(input())


for i in range(n):
    number = int(input())
    for k in range(2, 65):
        num = convert(number, k)
        if is_true(num):
            print(1)
            break
        
        if k == 64:
            print(0)
