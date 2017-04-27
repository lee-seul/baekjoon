# coding: utf-8


def the_number(num, cnt):
    num *= 3
    if num % 2:
        odd_even = "odd"
        num //= 2
    else:
        odd_even = "even"
        num += 1
        num //= 2

    num *= 3
    num //= 9

    print("{}. {}".format(cnt, odd_even), end=" ")
    print(num)

cnt = 1
while True:
    n = int(input())

    if not n:
        break

    the_number(n, cnt)
    cnt += 1

