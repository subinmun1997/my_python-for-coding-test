def solution(prices):
    answer = []
    for i in range(len(prices)):
        temp = prices[i]
        count = 0
        for j in range(i+1, len(prices)):
            if temp <= prices[j]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)

    return answer

print(solution([1,2,3,2,3]))