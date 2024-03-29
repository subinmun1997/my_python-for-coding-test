import heapq

n = int(input())

heap = []
for _ in range(n):
    nums = list(map(int, input().split()))

    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    else:
        for num in nums:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])