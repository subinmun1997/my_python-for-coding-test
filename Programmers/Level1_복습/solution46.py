def solution(absolutes, signs):
    answer = 0
    for absolutes, signs in zip(absolutes, signs):
        if signs:
            answer += absolutes
        else:
            answer -= absolutes

    return answer


print(solution([4,7,12], [True, False, True]))
print(solution([1,2,3], [False, False, True]))