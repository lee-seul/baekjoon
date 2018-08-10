# coding: utf-8


def check_bingo(matrix, left, right):
    count = 0
    if left.count(-1) == 5:
        count += 1
    if right.count(-1) == 5:
        count += 1

    for i in range(5):
        if matrix[i].count(-1) == 5:
            count += 1
        temp = []
        for j in range(5):
            temp.append(matrix[j][i])

        if temp.count(-1) == 5:
            count += 1

    return count >= 3


matrix = []

for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

left = []
right = []
for i in range(5):
    left.append(matrix[i][i])
    right.append(matrix[4-i][i])


call_number = []
for _ in range(5):
    numbers = list(map(int, input().split()))
    call_number.extend(numbers)


FOUND = False
for i, num in enumerate(call_number):
    for j in range(5):
        if right[j] == num:
            right[j] = -1
        if left[j] == num:
            left[j] = -1

        for k in range(5):
            if matrix[j][k] == num:
                matrix[j][k] = -1

            if check_bingo(matrix, left, right):
                FOUND = True
                print(i+1)
                break
        if FOUND:
            break
    if FOUND:
        break 

