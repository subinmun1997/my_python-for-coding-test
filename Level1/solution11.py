def solution(lottos, win_nums):
    _lottos = [l for l in lottos if l in win_nums]
    minc = len(_lottos) # 최저 갯수
    zero = lottos.count(0)
    maxc = minc + zero # 최대 갯수

    min_rank = 7 - minc # 최저 등수
    max_rank = 7 - maxc # 최고 등수

    if min_rank == 7:
        min_rank = 6
    if max_rank == 7:
        max_rank = 6

    return [max_rank, min_rank]
