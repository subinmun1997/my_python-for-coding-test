def pos(now):
    for j in range(1, n):
        # 낮은 칸과 높은 칸의 높이 차이는 1이하여야 한다.
        if abs(now[j] - now[j-1]) > 1:
            return False
        # 현 위지 보다 이전 위치의 높이가 더 높은 경우
        # 오른쪽을 기준으로 경사로 놓을 수 있는 지 파악
        if now[j] < now[j-1]:
            for k in range(l):
                # 범위를 벗어나거나 or 이미 놓은 곳이거나 or 칸의 높이가 다르다면
                if j+k >= n or used[j+k] or now[j] != now[j+k]:
                    return False
                # 높이가 동일하다면 경사로 놓기
                if now[j] == now[j+k]:
                    used[j+k] = True
        # 현 위치가 이전 위치보다 높이가 더 높은 경우
        # 왼쪽을 기준으로 경사로 놓을 수 있는 지 파악
        elif now[j] > now[j-1]:
            for k in range(l):
                # 범위를 벗어나거나 or 이미 놓은 곳이거나 or 칸의 높이가 다르다면
                if j-1-k < 0 or used[j-1-k] or now[j-1] != now[j-1-k]:
                    return False
                if now[j-1] == now[j-1-k]:
                    used[j-1-k] = True

    return True

# n=격자의 크기, l=경사로의 길이
n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 지나갈 수 있는 길의 개수
result = 0

# 지나갈 수 있는 가로의 개수 구하기
for i in range(n):
    used = [False for _ in range(n)]
    if pos(graph[i]):
        result += 1

# 지나갈 수 있는 세로의 개수 구하기
for i in range(n):
    used = [False for _ in range(n)]
    if pos([graph[j][i] for j in range(n)]):
        result += 1

print(result)