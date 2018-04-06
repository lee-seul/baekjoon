# coding: utf-8


def reverse_word(string):
    string = string.split()
    result = []
    for word in string:
        if word:
            word = list(word)
            word.reverse()
            word = ''.join(word)
            result.append(word)
    return ' '.join(result)


t = int(input())

for _ in range(t):
    string = input()
    reverse_string = reverse_word(string)
    if reverse_string:
        print(reverse_string)
