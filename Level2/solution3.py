def solution(arr):
    res = max(arr)

    while True:
        answer = 0
        for i in arr:
            if res%i == 0:
                answer += 1
            else:
                break

        if answer == len(arr):
            break
        res += 1
    return res

print(solution([2,6,8,14]))
print(solution([1,2,3]))