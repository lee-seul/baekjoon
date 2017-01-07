# coding: utf-8

n = int(input())

val = 1
x = 2
y = 1
result = 1
while True:
    if val == x:
        if x == 2:
            result += 1
            y *= 6
            x += y
        else:
            result += 1
            y += 6
            x += y
    val += y
    if val == n:
        result += 1
        break
    elif val > n:
        break


print(result)


