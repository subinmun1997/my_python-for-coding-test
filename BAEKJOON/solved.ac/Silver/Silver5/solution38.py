day = 0
while True:
    L, P, V = map(int, input().split())

    day += 1
    if L == 0 and  P == 0 and V == 0:
        break
    max_day = (V//P) * L + min(L, (V%P))
    print(f"Case {day}: {max_day}")