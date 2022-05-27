while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    score = {}
    for _ in range(n):
        num = list(map(int, input().split()))
        for i in num:
            if i in score:
                score[i] += 1
            else:
                score[i] = 1
    item = sorted(score.items(), key=lambda x : x[1], reverse=True)

    f_num, f_win = item[0]
    for num, win in item:
        if f_win != win:
            check = win
            break
    answer = []
    for num, win in item:
        if win == check:
            answer.append(num)
    print(*sorted(answer))
