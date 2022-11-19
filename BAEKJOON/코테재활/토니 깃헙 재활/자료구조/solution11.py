t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))
    check = [False for _ in range(n)]
    check[m] = True

    answer = 0
    while True:
        if seq[0] == max(seq):
            answer += 1
            if check[0]:
                print(answer)
                break
            else:
                seq.pop(0)
                check.pop(0)
        else:
            seq.append(seq.pop(0))
            check.append(check.pop(0))
