def dfs(x, y):
    global cnt
    # 범위를 벗어난다면 false
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    # 범위 내이고 해당 위치에 집이 있다면 1을 증가시키고, 해당 위치를 0으로 바꾼 후에 상하좌우 살펴보기
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True

    return False

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

village = 0 # 총 단지 수
cnt = 0 # 각 단지내 집의 수 찾기 위한 임시 변수
house = [] # 각 단지 내 집의 수
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            village += 1
            house.append(cnt)
            cnt = 0

print(village)
house.sort()
for h in house:
    print(h)