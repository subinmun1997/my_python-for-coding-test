def solution(d, budget):
    d.sort()

    cost = 0
    answer = 0
    for i in d:
        cost += i
        if cost <= budget:
            answer += 1
        else:
            break
    return answer

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))

