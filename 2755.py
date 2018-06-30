# coding: utf-8


n = int(input())

grades = {
    'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0
}

sum_point = 0
total = 0
for _ in range(n):
    _, point, grade = input().split()
    point = int(point)
    sum_point += point
    
    temp = grades[grade[0]]
    if not grade[0] == 'F':
        if grade[1] == '+':
            temp += 0.3
        if grade[1] == '-':
            temp -= 0.3
        
        total += point * temp 

result = round((total/sum_point) * 100) / 100
print('{:.2f}'.format(result))

