def dfs(x, y):
    global cnt
    # 범위 밖이라면 false
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1: # 해당 위치가 집이라면 0으로 바꿔주고 1증가시킴
        graph[x][y] = 0
        cnt += 1
        # 상하좌우 재귀탐색
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True

    return False

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

village = 0 # 총 단지 수
house = [] # 각 단지내 집의 수
cnt = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            village += 1 # 단지 수 하나 증가
            house.append(cnt) # 단지 내 집의 수 저장하고 다시 0으로 초기화
            cnt = 0

print(village)
for i in sorted(house):
    print(i)