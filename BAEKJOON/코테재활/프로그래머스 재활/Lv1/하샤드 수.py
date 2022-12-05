def solution(arr):
    num = sum(int(i) for i in str(arr))
    return False if arr%num else True

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))