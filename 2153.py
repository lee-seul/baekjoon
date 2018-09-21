# coding: utf-8


def is_prime(num):
    if num <= 2:
        return True 
    for i in range(2, num):
        if not num % i:
            return False
    return True


chars = {chr(x):x-38 for x in range(65, 91)}
chars.update({chr(x):x-96 for x in range(97, 123)})


string = input()
value = 0
for char in string:
    value += chars[char]
print(value)

if is_prime(value):
    print('It is a prime word.')
else:
    print('It is not a prime word.')

