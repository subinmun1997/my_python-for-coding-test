def pos(now):
    for j in range(1, n):
        if abs(now[j] - now[j-1]) > 1: # 1. 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
            return False
        if now[j] < now[j-1]: # 현재 < 이전; 오른쪽을 기준으로 경사로를 놓을 수 있는지 탐색
            for k in range(l): # 경사로는 l개의 칸이 연속되어 있어야 한다.
                # 현 위치 + 경사로의 길이가 배열을 넘어가거나 or 이미 배열이 놓여있거나 or 높이가 다르다면
                if j+k >= n or used[j+k] or now[j] != now[j+k]:
                    return False
                if now[j] == now[j+k]: # 경사로를 놓을 칸의 높이가 같다면
                    used[j+k] = True
        elif now[j] > now[j-1]: # 현재 > 이전; 왼쪽을 기준으로 경사로를 놓을 수 있는지 탐색
            for k in range(l):
                if j-1-k < 0 or used[j-1-k] or now[j-1] != now[j-1-k]:
                    return False
                if now[j-1] == now[j-1-k]:
                    used[j-1-k] = True

    return True

# 입력 조건
n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 출력 조건: 지나갈 수 있는 길의 개수
count = 0

# 지나갈 수 있는 행의 개수
for i in range(n):
    used = [False for _ in range(n)]
    if pos(graph[i]):
        count += 1

# 지나갈 수 있는 열의 개수
for i in range(n):
    used = [False for _ in range(n)]
    if pos([graph[j][i] for j in range(n)]):
        count += 1

print(count)