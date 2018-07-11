# coding: utf-8


def to_encoding(string):
    charsets = [
        ("%", "%25"), ("(", "%28"), (")", "%29"),
        (" ", "%20"), ("!", "%21"), ("$", "%24"), 
        ("*", "%2a")
    ]
    for charset in charsets:
        string = string.replace(charset[0], charset[1])
    return string


while True:
    s = input()
    if s == '#':
        break
    
    print(to_encoding(s))
