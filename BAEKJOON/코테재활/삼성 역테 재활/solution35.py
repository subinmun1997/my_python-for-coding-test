def pos(now):
    for j in range(1, n):
        # 칸의 높이 차이가 1이 아니라면
        if abs(now[j] - now[j-1]) > 1:
            return False
        if now[j] < now[j-1]: #현재 < 이전: 오른쪽 경사로 세울 수 있는지 확인
            for k in range(l):
                # 범위를 벗어나거나 or 이미 경사로를 놓은 곳이거나 or 칸의 높이가 같지 않다면
                if j+k >= n or used[j+k] or now[j] != now[j+k]:
                    return False
                # 칸의 높이가 같다면 경사로 놓기
                if now[j] == now[j+k]:
                    used[j+k] = True
        elif now[j] > now[j-1]: #현재 > 이전: 왼쪽 경사로 세울 수 있는지 확인
            for k in range(l):
                # 범위를 벗어나거나 or 이미 경사로를 놓은 곳이거나 or 칸의 높이가 같지 않다면
                if j-1-k < 0 or used[j-1-k] or now[j-1] != now[j-1-k]:
                    return False
                # 칸의 높이가 같다면 경사로 놓기
                if now[j-1] == now[j-1-k]:
                    used[j-1-k] = True

    return True

# 입력 조건 n=그래프 크기, l=경사로 길이
n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 출력 조건: 지나갈 수 있는 길의 개수
result = 0
# 지나갈 수 있는 행 개수 세기
for i in range(n):
    used = [False for _ in range(n)]
    if pos(graph[i]):
        result += 1

# 지나갈 수 있는 열 개수 세기
for i in range(n):
    used = [False for _ in range(n)]
    if pos([graph[j][i] for j in range(n)]):
        result += 1

print(result)