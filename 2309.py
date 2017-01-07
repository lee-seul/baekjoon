# coding: utf-8

height = []
for _ in range(9):
    height.append(int(input()))

for i in range(8):
    for j in range(i+1, 9):
        tmp = height.copy()
        tmp.remove(height[i])
        tmp.remove(height[j])
        if sum(tmp) == 100:
            break
    if sum(tmp) == 100:
        break

tmp.sort()
for i in range(7):
    print(tmp[i])

