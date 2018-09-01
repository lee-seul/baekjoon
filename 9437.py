# coding: utf-8 


while True:
    n = [int(x) for x in input().split()]
    if n[0] == 0:
        break
    n, p = n
    start, end = 1, n
    while end >= start:
        temp = [start, start+1, end-1, end]
        if p in temp:
            temp.remove(p)
            print(' '.join(map(str, temp)))
            break
        start += 2
        end -= 2
