# coding: utf-8

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    a %= 10
    if a:
        num = a
        l = [num]
        for _ in range(b):
            num = (num * a) % 10
            if num in l:
                break
            else:
                l.append(num)
        print(l[b%len(l)-1])
    else:
        print(10)
