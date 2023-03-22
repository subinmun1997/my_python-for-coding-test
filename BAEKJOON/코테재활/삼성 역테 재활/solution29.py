'''
백준 14889 - 스타트와 링크
combinations 안 쓰고 dfs로 풀이
'''
def dfs(depth, idx):
    global result
    # n//2명씩 두 개의 팀으로 나눴다면
    if depth == n//2:
        # 각 팀 능력치 값 0으로 초기화
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                # (i값과 j값이 True인 것들끼리 한 팀)
                if visited[i] and visited[j]:
                    power1 += ability[i][j]
                # (i값과 j값이 False인 것들끼리 한 팀)
                elif not visited[i] and not visited[j]:
                    power2 += ability[i][j]

        result = min(result, abs(power1 - power2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

# 입력 조건
n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
# 스타트 팀과 링크 팀 나누기 위한 bool 배열
visited = [False for _ in range(n)]

result = int(1e9)
dfs(0, 0)

print(result)