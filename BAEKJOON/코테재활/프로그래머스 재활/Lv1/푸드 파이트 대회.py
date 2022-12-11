def solution(food):
    answer = ''
    for idx, f in enumerate(food):
        for i in range(food[idx] // 2):
            answer += str(idx)
    answer += '0'
    answer += answer[-2:-len(answer)-1:-1]
    return answer

print(solution([1,3,4,6]))
print(solution([1,7,1,2]))
