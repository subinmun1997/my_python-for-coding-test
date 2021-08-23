def score(scores):
    if scores >= 90:
        return 'A'
    elif scores >= 80:
        return 'B'
    elif scores >= 70:
        return 'C'
    elif scores >= 50:
        return 'D'
    else:
        return 'F'

def solution(scores):
    answer = ''
    k = len(scores)
    arr = [[] for _ in range(k)]
    for i in range(k):
        for j in range(k):
            arr[i].append(scores[j][i])
    for i in range(k):
        if arr[i][i] == max(arr[i]) or arr[i][i] == min(arr[i]):
            if arr[i].count(arr[i][i]) == 1:
                arr[i][i] = 'X'

    for i in range(k):
        cnt = 0
        SUM = 0
        for j in range(k):
            if arr[i][j] != 'X':
                cnt += 1
                SUM += arr[i][j]
        answer += score(SUM/cnt)

    return answer

print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))