# coding: utf-8 


n = int(input())

contest = []
for _ in range(n):
    c, s, p = map(int, input().split())
    temp = {
        'contry': c,
        'student': s, 
        'point': p
    }
    contest.append(temp)

contest = sorted(contest, key=lambda data: data['point'], reverse=True)

first = contest[0]
second = contest[1]
third = contest[2]
if first['contry'] == second['contry'] == third['contry']:
    third = contest[3]

result = [first, second, third]

for d in result:
    print(d['contry'], d['student'])

