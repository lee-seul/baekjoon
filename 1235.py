# coding: utf-8 


n = int(input())

students = []
for _ in range(n):
    student = input()
    students.append(student)

length = len(student)

for i in range(1, length):
    temp = set(s[length-i:] for s in students)
    if len(temp) == n:
        print(i)
        break
    if i == length - 1:
        print(length)
        break

