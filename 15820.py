# coding: utf-8


s1, s2 = map(int, input().split())

sample = True
system = True
for _ in range(s1):
    a, b = map(int, input().split())
    if a != b:
        sample = False

for _ in range(s2):
    a, b = map(int, input().split())
    if a != b:
        system = False

if sample and system:
    print('Accepted')
if sample and not system:
    print('Why Wrong!!!')
if not sample:
    print('Wrong Answer')
