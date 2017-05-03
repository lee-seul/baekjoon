# coding: utf-8


def read_letter(string):
    length = len(string) ** 0.5
    length = int(length)
    temp = []
    for i in range(length):
        start = length * i
        end = start + length
        s = string[start:end]
        temp.append(s)

    letter = []
    for j in range(length):
        item = []
        for i in range(length):
            item.append(temp[i][j])
       
        letter.append(item)
    letter.reverse()
    result = ""
    for i in range(length):
        for j in range(length):
            result += letter[i][j]
    
    return result


n = int(input())

for _ in range(n):
    letter = input()
    letter = read_letter(letter)
    print(letter)

