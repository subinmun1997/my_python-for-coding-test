def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            continue
        elif (ord(s[i])+n) < (65+26):
            answer += chr(ord(s[i]) + n)
        elif (ord(s[i])+n) < (97+26) and ord(s[i]) >= 97:
            answer += chr(ord(s[i]) + n)
        else:
            answer += chr(ord(s[i]) +n-26)

    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))