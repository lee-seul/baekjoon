# coding: utf-8


n = int(input())

t = [[x, 0] for x in range(1, n+1)]
games = (n * (n - 1)) // 2


for _ in range(games):
    a, b, c, d = [int(i) for i in input().split()]
    if c > d:
        t[a-1][1] += 3
    if c == d:
        t[a-1][1] += 1
        t[b-1][1] += 1
    if c < d:
        t[b-1][1] += 3

points = [x[1] for x in t]
points.sort(reverse=True)
ranks = []
for x in t:
    idx = points.index(x[1])
    ranks.append(idx+1)


for r in ranks:
    print(r)
