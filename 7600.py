# coding: utf-8

l = [chr(i) for i in range(97, 123)]

while True:
    s = input().lower()
    if s == "#":
        break
    result = 0
    for c in l:
        if c in s:
            result += 1
    print(result)
