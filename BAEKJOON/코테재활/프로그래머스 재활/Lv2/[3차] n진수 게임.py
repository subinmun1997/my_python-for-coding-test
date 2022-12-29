def solution(n, t, m, p):
    answer = ''
    for i in range(t*m):
        answer += convert(i, n)

    answer = answer[:t*m]
    return answer[p-1::m]

def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))