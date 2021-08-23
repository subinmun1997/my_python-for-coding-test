def solution(progresses, speeds):
    answer = []
    count = 0
    day = 0
    while len(progresses) > 0:
        if (progresses[0]+speeds[0]*day) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            day += 1
    answer.append(count)
    return answer

print(solution([93,30,55],[1,30,5]))
print(solution([95,90,99,99,80,99],[1,1,1,1,1,1]))