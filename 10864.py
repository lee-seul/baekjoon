# coding: utf-8 


import sys 


temp = sys.stdin.readline().strip()

n, m = map(int, temp.split())

students = [0 for _ in range(n)] 

for _ in range(m):
    string = sys.stdin.readline().strip() 
    a, b = map(int, string.split())
    students[a-1] += 1
    students[b-1] += 1

for student in students:
    sys.stdout.write(str(student) + '\n')
