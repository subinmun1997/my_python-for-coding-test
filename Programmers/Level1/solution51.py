def solution(n, stages):
    file_rate = []
    st = len(stages)
    for i in range(1, n+1):
        user = stages.count(i)
        if user > 0:
            file_rate.append((i,user/st))
        else:
            file_rate.append((i, 0))
        st -= user

    file_rate.sort(key=lambda x : (-x[1], x[0]))

    answer = []
    for key, value in file_rate:
        answer.append(key)
    return answer


print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, [4,4,4,4,4]))
print(solution(3, [1,1,1]))