def solution(s):
    words = s.split(' ')
    result = ''
    for word in words:
        for j in range(len(word)):
            if j == 0:
                result += word[j].upper()
            else:
                result += word[j].lower()
        result += ' '
    return result

print(solution("3people unFollowed me"))
print(solution("for the last week"))