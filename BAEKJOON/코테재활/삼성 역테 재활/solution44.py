def spring_summer():
    for x in range(n):
        for y in range(n):
            # 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다
            if tree[x][y]:
                tree[x][y].sort()
                temp_live_tree = [] # 양분 먹고 나이가 1 증가한 새로운 나무 배열
                death = 0 # 봄에 죽은 나무는 양분으로 변한다

                for age in tree[x][y]:
                    # 나무는 자신의 나이만큼 양분을 먹고
                    if age <= origin_oil[x][y]:
                        origin_oil[x][y] -= age
                        # 나이가 1 증가한다
                        age += 1
                        temp_live_tree.append(age)
                    else: # 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 죽고, 양분으로 변함
                        death += age // 2

                # 죽은 나무 나이 // 2 만큼 나무가 있던 칸에 양분으로 추가된다
                origin_oil[x][y] += death
                tree[x][y] = []
                tree[x][y].extend(temp_live_tree)

def fall():
    # 가을에는 나무가 번식한다
    for x in range(n):
        for y in range(n):
            if tree[x][y]:
                for age in tree[x][y]:
                    # 번식하는 나무는 나이가 5의 배수이어야 한다
                    if age % 5 == 0:
                        # 인접한 범위 내 8개의 칸에 나이가 1인 나무 번식
                        for dir in range(8):
                            nx = x + dx[dir]
                            ny = y + dy[dir]

                            if 0 <= nx < n and 0 <= ny < n:
                                tree[nx][ny].append(1)

def winter():
    # 겨울에는 땅에 양분이 추가된다
    for x in range(n):
        for y in range(n):
            origin_oil[x][y] += plus_oil[x][y]

# 입력 조건
n, m, k = map(int, input().split())
# A배열의 값 = 각 칸에 추가되는 양분의 양 리스트
plus_oil = [list(map(int, input().split())) for _ in range(n)]
# 가장 처음에 양분은 모든 칸에 5만큼 들어있다
origin_oil = [[5 for _ in range(n)] for _ in range(n)]
# 각 칸에 심을 묘목들 저장하기 위한 배열, 하나의 칸에 여러 개의 나무가 있을 수 있기 때문에
# 각각의 리스트로 선언
tree = [[[] for _ in range(n)] for _ in range(n)]

# 상, 하, 좌, 우, 대각선 방향 선언
dx = [-1, 0, 1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

# 심은 나무 m개의 정보
for _ in range(m):
    x, y, z = map(int, input().split())
    # x좌표, y좌표, 나무의 나이
    tree[x-1][y-1].append(z)

# k년 동안 반복
for _ in range(k):
    spring_summer()
    fall()
    winter()

# 출력 조건
result = 0
for x in range(n):
    for y in range(n):
        # 살아있는 나무의 개수 더해주기
        result += len(tree[x][y])

print(result)