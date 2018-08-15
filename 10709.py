# coding: utf-8


h, w = map(int, input().split())

weather = []
for _ in range(h):
    status = input()
    weather.append(status)


for i in range(h):
    cloud = -1
    for j in range(w):
        if weather[i][j] == 'c':
            cloud = 0
        
        if weather[i][j] == '.' and cloud >= 0:
            cloud += 1

        print(cloud, end=' ')
    print()

