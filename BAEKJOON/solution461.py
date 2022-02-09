n = int(input())

money = []
for _ in range(n):
    dice = [0] * 7
    data = list(map(int, input().split()))

    for d in data:
        dice[d] += 1

    if 4 in dice:
        answer = 50000 + dice.index(4) * 5000
        money.append(answer)
    elif 3 in dice:
        answer = 10000 + dice.index(3) * 1000
        money.append(answer)
    elif dice.count(2) == 2:
        check = []
        for n, count in enumerate(dice):
            if count == 2:
                check.append(n)

        answer = 2000 + check[0] * 500 + check[1] * 500
        money.append(answer)
    elif 2 in dice:
        answer = 1000 + dice.index(2) * 100
        money.append(answer)
    else:
        check = []
        for n, count in enumerate(dice):
            if count == 1:
                check.append(n)
        if len(check) == 4:
            answer = max(data) * 100
            money.append(answer)

print(max(money))