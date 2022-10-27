t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))

    seq = [False for _ in range(n)]
    seq[m] = True

    answer = 0
    while True:
        if q[0] == max(q):
            answer += 1
            if seq[0]:
                print(answer)
                break
            else:
                q.pop(0)
                seq.pop(0)
        else:
            q.append(q.pop(0))
            seq.append(seq.pop(0))