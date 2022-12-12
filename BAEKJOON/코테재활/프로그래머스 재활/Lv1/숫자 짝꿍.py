def solution(x, y):
    answer = ''
    for i in range(9, -1, -1):
        answer += str(i) * min(x.count(str(i)), y.count(str(i)))

    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer

print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))