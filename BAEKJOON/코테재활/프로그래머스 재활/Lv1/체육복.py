def solution(n, lost, reserve):
    _lost = sorted(i for i in lost if i not in reserve)
    _reserve = sorted(i for i in reserve if i not in lost)

    for i in _reserve:
        left = i-1
        right = i+1
        if left in _lost:
            _lost.remove(left)
        elif right in _lost:
            _lost.remove(right)

    return n - len(_lost)

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))