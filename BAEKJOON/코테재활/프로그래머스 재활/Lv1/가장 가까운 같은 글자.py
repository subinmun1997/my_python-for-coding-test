def solution(s):
    answer = []
    idx_dict = {}

    for idx, i in enumerate(s):
        if i in idx_dict:
            answer.append(idx - idx_dict[i])
            idx_dict[i] = idx
        else:
            answer.append(-1)
            idx_dict[i] = idx
    return answer

print(solution("banana"))
print(solution("foobar"))