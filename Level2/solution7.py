def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer

# 한 줄 코드

# def solution(A,B):
#   return sum(a*b for a,b in zip(sorted(A), sorted(B, reverse=True))
