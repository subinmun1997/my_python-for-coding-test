from collections import deque

def solution(maps):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            elif maps[nx][ny] == 0:
                continue
            elif maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))


    result = maps[len(maps)-1][len(maps[0])-1]
    return -1 if result == 1 else result

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))