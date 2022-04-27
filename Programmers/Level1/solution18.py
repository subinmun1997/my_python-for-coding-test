def solution(s):
    # split()은 공백이 1개이건 2개이건 n개이건 상관없이 무조건 1개로 보고 처리
    # split(' ')은 공백 1개를 각각의 공백으로 따로 처리
    s = s.split(' ')
    answer = ''
    for i in s:
        for j in range(len(i)):
            if j%2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '

    return answer[0:-1]
print(solution("try hello world"))
