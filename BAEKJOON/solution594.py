t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    stikers = {}
    for i in range(m+1): # 스티커 종류 0으로 초기화
        stikers[i] = 0

    prize = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        prize.append(temp)

    coach = list(map(int, input().split()))
    for i in range(1, m+1):
        stikers[i] = coach[i-1]

    prize_money = 0
    for i in prize:
        check = True
        while True:
            for j in range(1, len(i) - 1):
                if stikers[i[j]] > 0:
                    stikers[i[j]] -= 1
                else:
                    check = False
            if check:
                prize_money += i[-1]
            else:
                break

    print(prize_money)