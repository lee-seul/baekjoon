# coding: utf-8

def judge(y):
    r = y.count(0)
    if r == 1:
        return "A"
    elif r == 2:
        return "B"
    elif r == 3:
        return "C"
    elif r == 4:
        return "D"
    else:
        return "E"

result = []

for _ in range(3):
    y = list(map(int, input().split()))
    result.append(judge(y))

for a in result:
    print(a)

