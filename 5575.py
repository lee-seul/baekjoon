# coding: utf-8


def cal_time(h, m, s, *out):
    result = [h, m, s]
    for i in range(3):
        result[i] = out[i] - result[i]
   
    for i in range(2, 0, -1):
        if result[i] < 0:
            result[i] = 60 + result[i]
            result[i-1] -= 1

    return result

result = []
for _ in range(3):
    time = map(int, input().split())
    temp = cal_time(*time)
    result.append(temp)

for r in result:
    print(r[0], r[1], r[2])

