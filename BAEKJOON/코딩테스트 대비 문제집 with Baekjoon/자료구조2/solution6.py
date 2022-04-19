import heapq

t = int(input())
for i in range(t):
    k = int(input())
    max_heap = []
    min_heap = []
    visited = [False] * k

    for j in range(k):
        data = input().split()
        if data[0] == "I":
            heapq.heappush(min_heap, (int(data[1]), j))
            heapq.heappush(max_heap, (-int(data[1]), j))
            visited[j] = True
        else:
            if int(data[1]) == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if len(min_heap) == 0 or len(max_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])

