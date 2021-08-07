def solution(s):
    answer = ''
    key = 0
    for i in range(len(s)):
        key += 1
        if s[i] == ' ':
            answer += ' '
            key = 0
            continue
        elif key%2 == 1:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer