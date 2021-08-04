def solution(strings, n):
    answer = []
    for s in strings:
        answer.append(s[n] + s)
    answer.sort()
    
    return [i[1:] for i in answer]
