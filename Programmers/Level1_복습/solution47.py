def solution(absolutes, signs):
    return sum(absolutes if signs else -absolutes for absolutes, signs in zip(absolutes, signs))


print(solution([4,7,12], [True, False, True]))
print(solution([1,2,3], [False, False, True]))