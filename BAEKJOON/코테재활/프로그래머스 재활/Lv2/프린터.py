def solution(priorities, location):
    pcheck = [False] * len(priorities)
    pcheck[location] = True

    result = 0
    while True:
        if priorities[0] == max(priorities):
            result += 1
            if pcheck[0]:
                break
            else:
                priorities.pop(0)
                pcheck.pop(0)
        else:
            priorities.append(priorities.pop(0))
            pcheck.append(pcheck.pop(0))

    return result

print(solution([2,1,3,2], 2))
print(solution([1,1,9,1,1,1], 0))
