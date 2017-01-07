# coding: utf-8

def check_score(num, average):
    if num > average:
        return 1
    return 0

n = int(input())

for _ in range(n):
    l = list(map(int, input().split()))
    ave = sum(l[1:])/l[0]
    count = sum(check_score(x, ave) for x in l[1:])
    print("{:.3f}%".format(count/(len(l)-1)*100))
