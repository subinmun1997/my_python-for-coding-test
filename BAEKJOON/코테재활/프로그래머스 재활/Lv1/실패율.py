def solution(n, stages):
    user = len(stages)
    answer = {x : 0 for x in range(1, n+1)}

    for i in range(1, n+1):
        if stages.count(i) > 0:
            answer[i] = stages.count(i) / user
        else:
            answer[i] = 0
        user -= stages.count(i)

    result = []
    answer = sorted(answer.items(), key=lambda x : (-x[1], x[0]))
    for x, y in answer:
        result.append(x)

    return result

print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, [4,4,4,4,4]))