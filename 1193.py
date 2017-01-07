# coding: utf-8

x = int(input())

row = 0 
col = 0
tem_row = 0
tem_col = 0
point = True
for i in range(1, x):
    if tem_col == row and tem_row == 0:
        tem_col += 1
        col = tem_col
        point = True 
    elif tem_row == col and tem_col == 0:
        tem_row += 1
        row = tem_row
        point = False
    else:
        if point:
            tem_col -= 1
            tem_row += 1
        else:
            tem_col += 1
            tem_row -=1
            
print("{}/{}".format(tem_row+1, tem_col+1))



