import math

def solution(progresses, speeds):
    time = []
    answer = []
    for i in range(len(progresses)):
        time.append(math.ceil((100-progresses[i])/speeds[i]))

    start = time[0]
    cnt = 1
    for i in range(1, len(time)):
        if time[i] <= start:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            start = time[i]

    answer.append(cnt)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))