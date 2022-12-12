def solution(s):
    answer = []
    c, nc = 0, 0
    x = s[0]
    temp = ''
    flag = False
    for i in s:
        if flag:
            x = i
            flag = False
        temp += i
        if x == i:
            c += 1
        else:
            nc += 1
        if c == nc:
            answer.append(temp)
            temp = ''
            flag = True
    if temp:
        answer.append(temp)
    return len(answer)

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))