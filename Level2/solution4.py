def solution(s):
    answer = ''.join(s.lower())
    res = ''
    res += answer[0].upper()

    for i in range(1, len(answer)):
        if answer[i] == " ":
            res += res.join("")
        if answer[i-1] == " ":
            res += res.join(answer[i].upper())
        else:
            res += res.join(answer[i])

    return res

print(solution("3people unFollowed me"))
print(solution("for the last week"))