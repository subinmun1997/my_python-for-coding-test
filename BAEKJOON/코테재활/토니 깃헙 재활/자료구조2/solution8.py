import heapq

n = int(input())

min_heap = []
max_heap = []
visited = [False] * 100001

for _ in range(n):
    num, level = map(int, input().split())
    heapq.heappush(min_heap, (level, num))
    heapq.heappush(max_heap, (-level, -num))
    visited[num] = True

m = int(input())
for _ in range(m):
    order = input().split()
    if order[0] == "add":
        heapq.heappush(min_heap, (int(order[2]), int(order[1])))
        heapq.heappush(max_heap, (-int(order[2]), -int(order[1])))
        visited[int(order[1])] = True
    elif order[0] == "recommend":
        if order[1] == "1":
            print(-max_heap[0][1])
        elif order[1] == "-1":
            print(min_heap[0][1])
    elif order[0] == "solved":
        visited[int(order[1])] = False
        while not visited[-max_heap[0][1]]:
            heapq.heappop(max_heap)
        while not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)