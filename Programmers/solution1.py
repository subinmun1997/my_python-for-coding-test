def solution(lottos, win_nums):
    _lottos = [l for l in lottos if l in win_nums]
    min_value = 7 - len(_lottos)
    if min_value == 7:
        min_value = 6

    zero = lottos.count(0)
    maximum = len(_lottos) + zero
    max_value = 7 - maximum

    print([max_value, min_value])

solution([44,1,0,0,31,25], [31,10,45,1,6,19])
solution([0,0,0,0,0,0], [38,19,20,40,15,25])
solution([45,4,35,20,3,9], [20,9,3,45,4,35])