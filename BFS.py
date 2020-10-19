from collections import deque

def bfs(graph,start,visited):
    queue = deque([start]) # 큐 구현을 위해 deque 라이브러리 사용
    visited[start] = True # 현재 노드 방문 처리

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i) # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

bfs(graph,1,visited)
