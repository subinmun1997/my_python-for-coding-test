def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'k')
    point = ['10' if i == 'k' else i for i in dartResult]

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt:
            answer[i] = answer[i] ** (sdt.index(j) + 1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0:
                answer[i-1] = answer[i-1] * 2
        elif j == '#':
            answer[i] = answer[i] * -1
        else:
            answer.append(int(j))
            i += 1

    return sum(answer)

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))