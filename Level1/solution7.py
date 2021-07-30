def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes
        else:
            answer -= absolutes
    return answer

# 한 줄 코드
# def solution(absolutes, signs):
#   return sum(absolutes if signs else -absolutes for absolutes, sign in zip(absolutes, signs))
