'''
백준 2606 바이러스 - BFS 풀이
'''

from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)] # 1번부터 n번 컴퓨터의 연결 정보 담기 위한 배열
visited = [False] * (n+1) # 방문여부 체크하기

# 연결 정보 입력하는 for문
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = 0
#  bfs로 그래프 탐색하면서 연결되어있는 컴퓨터 수 찾기
def bfs(graph, start, visited):
    global result
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                result += 1
                visited[i] = True
                queue.append(i)

bfs(graph, 1, visited)
print(result)