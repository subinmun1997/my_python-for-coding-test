def solution(s):
    answer = ''
    idx = 0
    for i in s:
        if idx%2 == 0:
            answer += i.upper()
            idx += 1
        else:
            answer += i.lower()
            idx += 1
        if i == ' ':
            idx = 0
    return answer

print(solution("try hello world"))
