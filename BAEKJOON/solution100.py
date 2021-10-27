t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))

    idx = [False for _ in range(len(q))]
    idx[m] = True

    order = 0

    while True:
        # 첫 번째가 우선순위라면
        if q[0] == max(q):
            # 첫 번째를 pop할 준비를 한다
            order += 1
            # 마침 첫 번째가 target이면 출력하고 종료
            if idx[0]:
                print(order)
                break
            else:
                q.pop(0)
                idx.pop(0)
        # 첫 번째가 우선순위가 낮으면 rotate
        else:
            q.append(q.pop(0))
            idx.append(idx.pop(0))
