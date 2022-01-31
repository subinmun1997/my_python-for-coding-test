k = int(input())
for _ in range(k):
    p, m = map(int, input().split())
    check = [True] * m
    reserve = []
    for _ in range(p):
        reserve.append(int(input()))

    count = 0
    for i in reserve:
        if check[i-1] == False:
            count += 1
        else:
            check[i-1] = False

    print(count)