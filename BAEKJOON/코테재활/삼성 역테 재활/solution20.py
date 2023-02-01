import sys
input = sys.stdin.readline

# 양분 그래프 n x n , m나무개수, k년이 지난 후
n, m, k = map(int, input().split())

# 나중에 겨울에 양분 추가해줄 그래프  = plus_soil
plus_soil = []
for _ in range(n):
    plus_soil.append(list(map(int, input().split())))

# 나무 양분 그래프
origin_soil = [[5] * n for _ in range(n)]


# 살아있는 나무 그래프
live = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int,input().split())
    live[x-1][y-1].append(z)

for _ in range(k):
    # 봄 + 여름
    for i in range(n):
        for j in range(n):
            if live[i][j] :
                # 봄에 나이가 어린 나무 부터 양분을 먹게하기위한 정렬
                live[i][j].sort()
                # live = [] # 살아있는 나무들 리스트를 알아야 가을에 번식을 할 수 있다.
                tmp_live_tree=[]
                death = 0
                for age in live[i][j]:
                    if age <= origin_soil[i][j]:
                        origin_soil[i][j] -= age
                        age += 1
                        tmp_live_tree.append(age)
                    else:
                        death += age // 2
                origin_soil[i][j] += death
                # 죽은건 죽은대로, 산건 산거대로 옮긴다.
                live[i][j] = []
                live[i][j].extend(tmp_live_tree)

    #가을
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(n):
        for j in range(n):
            if live[i][j]:
                for age in live[i][j]:
                    if age % 5 == 0:
                        for dir in range(8):
                            nx = i + dx[dir]
                            ny = j + dy[dir]
                            if 0 <= nx < n and 0 <= ny < n:
                                live[nx][ny].append(1)
    #겨울
    for i in range(n):
        for j in range(n):
            origin_soil[i][j] += plus_soil[i][j]

result = 0
for i in range(n):
    for j in range(n):
        result += len(live[i][j])
print(result)