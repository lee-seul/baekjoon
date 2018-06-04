# coding: utf-8 


import hashlib


s = input()
result = hashlib.sha224()
result.update(bytes(s, 'utf-8'))

print(result.hexdigest())
