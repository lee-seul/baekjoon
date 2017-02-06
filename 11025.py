# coding: utf-8

n, m = map(int, input().split())

people = [x for x in range(1, n+1)]

idx = m - 1
while len(people) != 1:
    print(len(people))
    people.pop(idx)
    idx += m - 1
    idx %= len(people)

print(people[0])
