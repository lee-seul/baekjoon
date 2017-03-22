# coding: utf-8

n = int(input())
result = [0 for _ in range(5)]

for _ in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        result[0] += 1
    elif x < 0 and y > 0:
        result[1] += 1
    elif x < 0 and y < 0:
        result[2] += 1
    elif x > 0 and y < 0:
        result[3] += 1
    else:
        result[4] += 1

for i in range(1, 6):
    if i < 5:
        print("Q{}: {}".format(i, result[i-1]))
    else:
        print("AXIS: {}".format(result[4]))

