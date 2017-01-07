# coding: utf-8

def is_dec(num):
    l = list(str(num))
    for i in range(len(l)-1):
        if int(l[i]) - int(l[i+1]) <= 0:
            l[i] = str(int(l[i]) + 1)
            for j in range(i+1, len(l)):
                l[j] = "0"
            return int("".join(l))
    return num

n = int(input())
cnt, i = 0, 1
result = -1
while i <= 9876543210:
    if is_dec(i) == i:
        cnt += 1
        if cnt == n:
            result = i
            break
        i += 1
    else:
        i = is_dec(i)
if n == 0:
    result = 0

print(result)
