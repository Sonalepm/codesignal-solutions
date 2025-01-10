def solution(s):
    s_new = []
    for i in s: 
        if 'a' <= i < 'z':
            i = chr(ord(i) + 1)
        elif i == 'z':
            i = 'a'
        elif 'A' <= i < 'Z':
            i = chr(ord(i) + 1)
        elif i == 'Z':
            i = 'A'
        s_new.append(i)
    return ''.join(s_new)