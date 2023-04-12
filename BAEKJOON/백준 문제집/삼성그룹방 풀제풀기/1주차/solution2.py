from collections import deque

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        # 현재 위치가 동생이 있는 위치라면
        if x == k:
            print(time[x])
            break
        # 현재 위치 x로부터 이동 가능한 위치는 x-1, x+1, x*2
        for i in (x-1, x+1, x*2):
            # 범위 내이고 방문했던 칸이 아니라면
            if 0 <= i <= 100000 and not time[i]:
                # 현재 위치 + 1 시간이 새로운 위치 i까지의 도달 시간
                time[i] = time[x] + 1
                queue.append(i)

# n=수빈이 위치, k=동생 위치
n, k = map(int, input().split())
# 점의 최대 위치는 100,000
time = [0] * 100001
bfs()