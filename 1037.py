# coding: utf-8


n = int(input())
l = list(map(int, input().split()))

s = max(l)

i = 2
not_found = True
while not_found:
    num = s *i
    for j in l:
        if num % j != 0:
            not_found = True
            break
        else:
            not_found = False
    if not not_found:
        for k in range(2, num//2 + 1):
            if num % k == 0 and k not in l:
                not_found = True
                break
            else:
                not_found = False
    i += 1

print(num)





