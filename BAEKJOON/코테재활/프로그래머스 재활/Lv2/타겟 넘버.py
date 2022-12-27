from itertools import product

def solution(numbers, target):
    num = [(x, -x) for x in numbers]
    s = list(map(sum, product(*num)))
    return s.count(target)

print(solution([1,1,1,1,1], 3))
print(solution([4,1,2,1], 4))

# [다른 풀이 - 재귀]
# def recursive(numbers, sum, target):
#     if numbers == []:
#         if sum == target:
#             return 1
#         else:
#             return 0
#     return recursive(numbers[1:], sum+numbers[0], target) + recursive(numbers[1:], sum-numbers[0], target)
#
# def solution(numbers, target):
#     return recursive(numbers, 0, target)