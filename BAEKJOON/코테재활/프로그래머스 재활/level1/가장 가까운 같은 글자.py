def solution(s):
    pos = dict()
    result = []
    for idx, w in enumerate(s):
        if w not in pos:
            result.append(-1)
        else:
            result.append(idx - pos[w])
        pos[w] = idx

    return result

print(solution("banana"))
print(solution("foobar"))
