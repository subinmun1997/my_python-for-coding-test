def solution(n, lost, reserve):
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)

    for r in _reserve:
        f = r-1
        b = r+1

        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)

    answer = n - len(lost)
    return answer

print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(3,[3],[1]))
