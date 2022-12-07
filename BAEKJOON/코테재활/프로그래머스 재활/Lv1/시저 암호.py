def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        elif i.islower():
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        else:
            answer += i
    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))