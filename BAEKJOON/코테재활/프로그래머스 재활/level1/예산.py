def solution(d, budget):
    d.sort()

    count = 0
    cost = 0
    for i in d:
        cost += i
        if cost <= budget:
            count += 1
        else:
            break

    return count

print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))