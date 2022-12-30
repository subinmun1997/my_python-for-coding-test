def solution(elements):
    numberSet = set()

    eleLen = len(elements)
    elements *= 2

    for i in range(1, eleLen+1):
        for j in range(eleLen):
            numberSet.add(sum(elements[j:j+i]))

    return len(numberSet)

print(solution([7,9,1,1,4]))

