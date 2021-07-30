from itertools import combinations as cb

def solution(nums):
    answer = 0
    for i in cb(nums, 3):
        res = sum(i)
        for j in range(2, res):
            if res%j == 0:
                break;
        else:
            answer += 1
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))