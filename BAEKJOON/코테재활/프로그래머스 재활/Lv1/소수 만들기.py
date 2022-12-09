from itertools import combinations

def solution(nums):
    count = 0
    for i in combinations(nums, 3):
        if check_prime(sum(i)):
            count += 1
    return count

def check_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))