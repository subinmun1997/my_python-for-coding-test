def solution(arr, divisor):
    answer = sorted(i for i in arr if i%divisor == 0)
    return answer if answer else [-1]

print(solution([5,9,7,10], 5))
print(solution([2,36,1,3], 1))
print(solution([3,2,6], 10))