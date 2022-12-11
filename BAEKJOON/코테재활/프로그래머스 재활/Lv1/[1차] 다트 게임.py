def solution(dartResult):
    # 1S2D*3T 1^1 * 2 + 2^2 * 2 + 3^3
    answer = []
    dartResult = dartResult.replace('10', 'K')
    point = ['10' if i == 'K' else i for i in dartResult]

    idx = -1
    sdt = ['S', 'D', 'T']
    for i in point:
        if i in sdt:
            answer[idx] = answer[idx] ** (sdt.index(i)+1)
        elif i == '*':
            answer[idx] = answer[idx] * 2
            if i != 0:
                answer[idx-1] = answer[idx-1] * 2
        elif i == '#':
            answer[idx] = answer[idx] * -1
        else:
            answer.append(int(i))
            idx += 1

    return sum(answer)

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))

