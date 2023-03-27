def solution(s):
    answer = []
    for i in s:
        if answer[-1:] == [i]:
            answer.pop()
        else:
            answer.append(i)
    return 0 if answer else 1

print(solution("baabaa"))
print(solution("cdcd"))