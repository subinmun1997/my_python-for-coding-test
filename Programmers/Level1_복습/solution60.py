def solution(new_id):
    answer = ''
    arr = ['-', '_', '.']

    #1단계
    new_id = new_id.lower()

    #2단계
    for i in new_id:
        if i.isalnum() or i in arr:
            answer += i
    #3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    #4단계
    if len(answer) >= 1:
        if answer[0] == '.':
            answer = answer[1:]
    if len(answer) >= 1:
        if answer[-1] == '.':
            answer = answer[:-1]

    #5단계
    if len(answer) == 0:
        answer += 'a'

    #6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    #7단계
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]

    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))