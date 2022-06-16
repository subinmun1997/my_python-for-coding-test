def solution(arr):
    return arr%sum(int(i) for i in str(arr)) == 0

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))