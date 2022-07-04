def solution(n, lost, reserve):
    _reserve = sorted(i for i in reserve if i not in lost)
    _lost = sorted(i for i in lost if i not in reserve)

    for i in _reserve:
        f = i-1
        b = i+1

        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)

    return n - len(_lost)

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))