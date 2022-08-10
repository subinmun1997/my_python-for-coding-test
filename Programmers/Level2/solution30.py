def solution(s):
    s = s.lower()
    result = ''
    result += s[0].upper()

    for i in range(1, len(s)):
        if s[i] == " ":
            result += " "
        elif s[i-1] == " ":
            result += s[i].upper()
        else:
            result += s[i].lower()

    return result

print(solution("3people unFollowed me"))
print(solution("for the last week"))