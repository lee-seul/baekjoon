# coding: utf-8

odd = []
for _ in range(7):
    num = int(input())
    if num % 2:
        odd.append(num)

if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)

