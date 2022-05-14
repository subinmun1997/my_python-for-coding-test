def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        word = ""
        cnt = 1
        prev = s[0:step]
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                cnt += 1
            else:
                word += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j:j+step]
                cnt = 1
        word += str(cnt) + prev if cnt >= 2 else prev

        answer = min(answer, len(word))
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))