# coding: utf-8

l, r, a = map(int, input().split())

member = [l, r]
member.sort()

ab = member[1] - member[0]

if ab and ab >= a:
    print((member[0]+a)*2)

if ab and ab < a:
    result = 2 * (member[0] + ab) 
    a -= ab
    a = (a//2) * 2
    print(result+a)

if ab == 0:
    result = member[0] * 2
    a = (a//2) * 2
    print(result+a)


