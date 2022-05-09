from itertools import combinations

def prime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        if prime(sum(i)):
            answer += 1
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
