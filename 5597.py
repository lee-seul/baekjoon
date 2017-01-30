# coding: utf-8

students = [x for x in range(31)]
for _ in range(28):
    students[int(input())] = 0

for student in students:
    if student:
        print(student)
