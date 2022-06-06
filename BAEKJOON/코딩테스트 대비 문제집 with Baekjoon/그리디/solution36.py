n, m = map(int, input().split())

if n == 0:
    print(0)
else:
    w = list(map(int, input().split()))
    answer = 1
    temp = 0
    for i in range(n):
        temp += w[i]
        if temp > m:
            answer += 1
            temp = w[i]

    print(answer)