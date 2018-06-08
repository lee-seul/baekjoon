# coding: utf-8 


import hashlib


s = input()
result = hashlib.new('ripemd160')
result.update(bytes(s, 'utf-8'))

print(result.hexdigest())
