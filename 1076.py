# coding: utf-8

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 
        'white']

input_list = []
for _ in range(3):
    input_list.append(input())

num = ""
num += str(color.index(input_list[0])) + str(color.index(input_list[1]))
print(int(num) * 10**color.index(input_list[2]))



