# coding: utf-8 


n = int(input())
results = [tuple(input().split()) for _ in range(n)]
results.sort()
results.reverse()

five = results[4]
results = results[5:]
count = 0
for result in results:
    if result[0] == five[0]:
        count += 1

print(count)
