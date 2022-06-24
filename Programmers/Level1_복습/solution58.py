def solution(lottos, win_nums):
    _lottos = [i for i in lottos if i in win_nums]
    min_cnt = len(_lottos)
    max_cnt = min_cnt + lottos.count(0)

    max_score = 7 - max_cnt
    min_score = 7 - min_cnt

    if max_score == 7:
        max_score = 6
    if min_score == 7:
        min_score = 6

    return [max_score, min_score]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))