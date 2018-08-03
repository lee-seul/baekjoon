# coding: utf-8

n = int(input())
peaks = list(map(int, input().split()))

result = 0
cnt = 0
start = peaks[0]
for i, peak in enumerate(peaks):
    if not i:
        continue

    if start > peak:
        cnt += 1
    else:
        start = peak
        if result < cnt:
            result = cnt
        cnt = 0

print(max(result, cnt))
    
