'''
[풀이 과정]
이 문제는 벽을 3개 설치하는 모든 경우의 수를 다 계산해야 한다.
전체 맵의 크기가 최대 8x8이므로, 벽을 설치할 수 있는 최악의 경우 64C3이다.
이는 100,000보다 작은 수이므로, 모든 경우의 수를 고려해도 제한 시간 안에 문제를 해결할 수 있다.

[풀이 순서]
1. DFS를 이용해 바이러스가 확산되도록 하는 함수를 만든다.
2. 안전거리 영역에 해당하는 점수를 세는 함수를 만든다.
3. DFS를 이용해 벽 3개를 설치하는 모든 경우의 수를 계산한다.
3-1. 벽을 3개 설치했다면 바이러스를 퍼뜨리고, 각 경우의 수(벽 3개)마다 비교하며
     안전 영역의 최댓값을 계산한다.
4. DFS를 실행한 다음, 결과값을 출력한다.
'''
def get_score():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1

    return cnt

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 1
                virus(temp, nx, ny)

# 입력 조건
n, m = map(int, input().split())
# 0=빈칸, 1=벽, 2=바이러스
graph = [list(map(int, input().split())) for _ in range(n)]
# deepcopy 용도로 임시 배열
temp = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
def dfs(count):
    global result
    # 벽 3개를 다 세웠으면 임시배열로 값을 옮기고 (deepcopy)
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                # 해당 위치가 바이러스라면 퍼트리기
                if temp[i][j] == 2:
                    virus(i, j)

        # 퍼트리기가 끝났으면 안전구역 구하기
        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)