def solution(s):
    answer = ''
    s = s.split(' ')
    for i in s:
        for j in range(len(i)):
            if j%2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer

print(solution("try hello world"))