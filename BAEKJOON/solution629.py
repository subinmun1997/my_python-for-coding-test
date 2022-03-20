import heapq
import sys

input = sys.stdin.readline

def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)  # 최대힙
        dist = -1 * dist

        if now == end:
            print(dist)
            break

        if distance[now] > dist: # 이미 최대 중량인경우
            continue

        for i in graph[now]: # 정렬된 상태이므로 높은 중량부터 탐색이 됨.
            if dist == 0: # dist가 0인게 문제여...
                distance[i[1]] = i[0]
                heapq.heappush(queue, (-distance[i[1]], i[1]))
            # 기존에 저장된 값이 dist(이전 도시에서의 최대중량)와 현재 다리 최대 중량 보다 작다면...
            # 이렇게 한 이유는 다리가 중복 연결되어있는 가능성이 있기 때문
            elif distance[i[1]] < i[0] and distance[i[1]] < dist:
                distance[i[1]] = min(dist, i[0]) # ✅ 이전도시 최대 중량과 현재 다리 최대 중량 중 작은 값을 저장
                heapq.heappush(queue, (-distance[i[1]], i[1]))



if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    for i in range(1, n + 1):
        graph[i].sort(reverse=True)

    distance = [0] * (n + 1)
    start, end = map(int, input().split())

    dijkstra(start, end)
