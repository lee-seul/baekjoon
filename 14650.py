# coding: utf-8


def get_start_number(n):
    base = 10 ** (n-1)
    max_number = 3 * base 
    start_number = base + (3-(base%3))
    return start_number, max_number


n = int(input())

start_number, max_number = get_start_number(n)
cnt = 0
rule = {'0', '1', '2'}
while start_number < max_number:
    if set(str(start_number)).issubset(rule):
        print(start_number)
        cnt += 1
    start_number += 3

print(cnt)
