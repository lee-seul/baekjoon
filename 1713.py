# coding: utf-8


n = int(input())
input()
s = []
cnt = [0 for x in range(101)]
for x in [int(x) for x in input().split()]:
    if x in s:
        cnt[x] += 1
    elif len(s) < n:
        s.append(x)
        cnt[x] += 1
    else:
        f = s[0]
        for k in s:
            if cnt[f] > cnt[f]:
                f = k
        s.remove(f)
        cnt[f] = 0
        s.append(x)
        cnt[x] += 1

for x in sorted(s): 
    print(x, end=' ')
