def solution(s):
    vowels = set('aAeEiIoOuU');
    result = []
    for ind,i in enumerate(s):
        if i in vowels:
            result.append(ind)
    return result
