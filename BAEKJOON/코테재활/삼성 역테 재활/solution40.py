# 입력 조건
n = int(input())
# 격자의 크기는 100 * 100
graph = [[0] * 101 for _ in range(101)]

# 드래곤 커브의 방향 0:우, 1:상, 2:좌, 3:하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(n):
    # x좌표와 y좌표가 뒤바껴 있으므로, 바꿔서 입력받기
    y, x, d, g = map(int, input().split())
    # 시작 위치 드래곤 커브로 체크
    graph[x][y] = 1

    # 드래곤 커브를 만들면서 이동하는 방향 저장해놓기
    curve = [d]
    # 세대만큼 반복
    for _ in range(g):
        # 새로운 드래곤 커브 방향은 직전 커브의 90도 회전한 방향
        for k in range(len(curve)-1, -1, -1):
            curve.append((curve[k] + 1) % 4)

    # 방향 더해주면서 격자위에 표시하기
    for i in range(len(curve)):
        x += dx[curve[i]]
        y += dy[curve[i]]
        graph[x][y] = 1

# 출력 조건
result = 0
for i in range(100):
    for j in range(100):
        # 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부라면
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
            result += 1

print(result)