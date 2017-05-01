# coding: utf-8


while True:
    numbers = list(map(int, input().split()))
    a = set(numbers)
    if len(a) == 1 and not numbers[0]:
        break
    cnt = 0
    while True:
        if len(set(numbers)) == 1:
            break
        temp = [0, 0, 0, 0]
        for i in range(4):
            temp[i] = numbers[i] - numbers[(i+1)%4]
            temp[i] = abs(temp[i])
        numbers = temp
        cnt += 1
    print(cnt)

