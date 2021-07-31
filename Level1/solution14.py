def solution(d, budget):
    answer = 0
    ans = 0
    d.sort()

    for i in d:
        answer += i
        ans += 1
        if answer > budget:
            break

    return ans

# 다른 코드
# def solution(d, budget):
#   d.sort()
#   while budget < sum(d):
#       d.pop()
#   return len(d)
