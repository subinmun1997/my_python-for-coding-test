import sys
input = sys.stdin.readline

count = 0
def solve(i, j):
    if j == c-1:
        return True
    for d in dx:
        if i+d >= 0 and i+d < r and grid[i+d][j+1] == '.' and not visited[i+d][j+1]:
            visited[i+d][j+1] = True
            if solve(i+d, j+1):
                return True
    return False

r, c = map(int, input().split())
grid = [input().rstrip() for _ in range(r)]
visited = [[False] * c for _ in range(r)]

dx = [-1,0,1] # 위로 앞으로 아래로
result = 0
for i in range(r):
    if grid[i][0] == '.':
        if solve(i,0):
            result += 1

print(result)


