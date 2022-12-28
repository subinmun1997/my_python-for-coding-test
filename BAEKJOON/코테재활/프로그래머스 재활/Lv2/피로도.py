from itertools import permutations

def solution(k, dungeons):
    dun_num = len(dungeons)
    answer = 0

    for permut in permutations(dungeons, dun_num):
        _k = k
        count = 0
        for pm in permut:
            if _k >= pm[0]:
                _k -= pm[1]
                count += 1
        if count > answer:
            answer = count

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))