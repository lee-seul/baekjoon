# coding: utf-8

while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    if not a % b:
        print("multiple")
    elif not b % a:
        print("factor")
    else:
        print("neither")
