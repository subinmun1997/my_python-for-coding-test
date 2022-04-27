def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif (ord(i)+n) < (65+26):
            answer += chr(ord(i)+n)
        elif (ord(i)+n) < (97+26) and ord(i) >= 97:
            answer += chr(ord(i)+n)
        else:
            answer += chr(ord(i)+n-26)
    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))