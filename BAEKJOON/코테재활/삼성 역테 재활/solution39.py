def check():
    # 0번 열부터 n-1번 열까지 하나씩 살펴보며 동일한 위치에서 끝나는지 확인
    for start in range(n):
        # 동일한 위치에서 끝나려면 k와 start가 일치해야함
        k = start
        for j in range(h):
            # 해당 위치가 True값이라면 가로선이 놓여져있는 것이니, 오른쪽으로 이동
            if graph[j][k]:
                k += 1
            # 해당 위치가 True값이라면 가로선이 놓여져있는 것이니, 왼쪽으로 이동
            elif k > 0 and graph[j][k-1]:
                k -= 1
        # 출발 위치와 도착 위치가 다르다면 False
        if k != start:
            return False

    return True

def dfs(count, x, y):
    global result

    # i번 세로선의 결과가 i번이 나온다면 추가해야 하는 가로선의 최소 개수 구하고 반환
    if check():
        result = min(result, count)
        return
    # count가 3개이면 다음번에 4개가 되기 때문에 or result보다 크면 의미가 없기 때문에 그대로 리턴
    if count == 3 or result <= count:
        return

    for i in range(x, h):
        # 같은 행이면 y번째 열부터 다시 시작
        if i == x:
            k = y
        # 행이 바꼈으면 0번째 열부터 다시 시작
        else:
            k = 0

        for j in range(k, n-1):
            # 현재 위치와 오른쪽 둘 다 가로선이 없으면 추가해보기
            if not graph[i][j] and not graph[i][j+1]:
                # 왼쪽에 가로선이 있다면 현재 위치는 pass
                if j > 0 and graph[i][j-1]:
                    continue
                graph[i][j] = True
                # 가로선이 서로 연속하는 경우는 없기 때문에 j+2
                dfs(count+1, i, j+2)
                graph[i][j] = False

# 입력 조건 n=세로선 수, m=가로선 수, h=세로선마다 가로선을 놓을 수 있는 위치의 개수
n, m, h = map(int, input().split())
# 가로선 여부 파악하기 위한 n * h 배열
graph = [[False] * n for _ in range(h)]

# 가로선 정보
for _ in range(m):
    a, b = map(int, input().split())
    # a번 점선 위치에서 (b, b+1)번 세로선 연결
    graph[a-1][b-1] = True

# 정답이 3보다 큰 값이면 -1를 출력해야 되기 때문에, 4로 초기화
result = 4
dfs(0, 0, 0) # 추가한 가로선의 수, x좌표, y좌표

print(result if result < 4 else -1)