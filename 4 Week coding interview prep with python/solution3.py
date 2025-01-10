def solution(input_string):
    s_new = []
    for i in input_string:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - 32)
        elif 'A' <= i <= 'Z':
            i = chr(ord(i) + 32)
        s_new.append(i)
    return ''.join(s_new)