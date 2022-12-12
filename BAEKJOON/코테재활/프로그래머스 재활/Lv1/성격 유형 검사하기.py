def solution(survey, choices):
    type = ["R", "T", "C", "F", "J", "M", "A", "N"]
    kbti = {x : 0 for x in type}
    for i in range(len(survey)):
        if choices[i] < 4:
            kbti[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            kbti[survey[i][1]] += choices[i] - 4

    answer = ""
    if kbti['R'] < kbti['T']:
        answer += 'T'
    else:
        answer += 'R'

    if kbti['C'] < kbti['F']:
        answer += 'F'
    else:
        answer += 'C'

    if kbti['J'] < kbti['M']:
        answer += 'M'
    else:
        answer += 'J'

    if kbti['A'] < kbti['N']:
        answer += 'N'
    else:
        answer += 'A'

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
