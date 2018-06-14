# coding: utf-8


import base64


s = input()
s = s.encode('utf-8')


result = base64.b16encode(s)
print(result.decode('utf-8'))
