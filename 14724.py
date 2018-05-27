# coding: utf-8


n = int(input())

keys = ['PROBRAIN', 'GROW', 'ARGOS', 
        'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']

rank = []

for key in keys:
    top = max(map(int, input().split()))
    temp_dict = {
        'name': key,
        'point': top
    }
    
    rank.append(temp_dict)

rank = sorted(rank, key=lambda n: n['point'], reverse=True)

print(rank[0]['name'])

