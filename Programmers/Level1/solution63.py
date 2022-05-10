def solution(lottos, win_nums):
    _lottos = [i for i in lottos if i in win_nums]
    min_value = len(_lottos) # 최저 개수
    max_value = min_value + lottos.count(0) # 최대 개수
    min_rank = 7 - min_value
    max_rank = 7 - max_value

    if min_rank == 7:
        min_rank = 6
    if max_rank == 7:
        max_rank = 6

    return [max_rank, min_rank]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))