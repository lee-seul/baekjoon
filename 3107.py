# coding: utf-8 

ip = input()

temp_ip = ip.replace('::', ':')
temp_ip = [x for x in temp_ip.split(':') if x]
real_length = 8 - len(temp_ip)

temp_ip_list = ip.split('::')
if len(temp_ip_list) != 1:
    temp = ''
    for i in range(real_length):
        temp += '0000'
        if i != real_length - 1:
            temp += ':'

    ip = temp_ip_list[0] + ':' + temp
    if temp_ip_list[1]:
        ip += ':' + temp_ip_list[1]
    

result = []
for chunk in ip.split(':'):
    length = len(chunk)
    zero = 4 - length
    temp = '0' * zero + chunk
    result.append(temp)

print(':'.join(result))
