def solution(d, budget):
    total = 0
    count = 0
    for i in sorted(d):
        total += i
        if total > budget:
            break
        count += 1
    return count

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))