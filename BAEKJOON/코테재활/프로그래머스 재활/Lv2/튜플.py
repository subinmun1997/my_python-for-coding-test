def solution(s):
    answer = []
    s = s[2:-2].replace('{','').replace(',',' ').split('}')
    for i, v in enumerate(s):
        s[i] = v.split()
    s.sort(key=lambda x : len(x))

    for num in s:
        for j in num:
            j = int(j)
            if j not in answer:
                answer.append(j)

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))