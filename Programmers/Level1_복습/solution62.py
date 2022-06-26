def solution(n, stages):
    user = len(stages)
    stage_rate = []

    for i in range(1, n+1):
        fail = stages.count(i)
        if fail > 0:
            stage_rate.append((i, fail/user))
        else:
            stage_rate.append((i, 0))
        user -= fail

    stage_rate.sort(key=lambda x : (-x[1], x[0]))

    answer = []
    for key, value in stage_rate:
        answer.append(key)
    return answer


print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, [4,4,4,4,4]))