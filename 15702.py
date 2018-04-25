# coding: utf-8


n, m = map(int, input().split())
points = list(map(int, input().split()))

tests = []
for _ in range(m):
    temp = input().split()
    tests.append(temp)


student = 0
point = 0
for test in tests:
    temp_point = 0
    for i, p in enumerate(test[1:]):
        if p == 'O':
            temp_point += points[i]

    if temp_point >= point:
        if temp_point == point and int(test[0]) > student and student != 0:
            continue
        point = temp_point
        student = int(test[0])
        
print(student, point)


