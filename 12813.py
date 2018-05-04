# coding: utf-8



a = input()
b = input()

result_and = ''
result_or = ''
result_xor = ''
result_not_a = ''
result_not_b = ''
for i in range(100000):
    if a[i] == '1' and b[i] == '1': 
        result_and += '1'
    else:
        result_and += '0' 

    if a[i] == '1' or b[i] == '1':
        result_or += '1'
    else:
        result_or += '0'

    if a[i] != b[i]:
        result_xor += '1'
    else:
        result_xor += '0'

    if a[i] == '1':
        result_not_a += '0'
    else:
        result_not_a += '1'

    if b[i] == '1':
        result_not_b += '0'
    else:
        result_not_b += '1'

print(result_and)
print(result_or)
print(result_xor)
print(result_not_a)
print(result_not_b)

