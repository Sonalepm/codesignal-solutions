def solution(s):
    s = list(s)
    for i in range(0,len(s)-1,2):
        s[i],s[i+1] = s[i+1],s[i]
            
    return ''.join(s)