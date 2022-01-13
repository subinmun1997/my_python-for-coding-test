import heapq

n = int(input())
numbers = [int(input()) for _ in range(n)]

heap = []
for i in numbers:
    heapq.heappush(heap, i)

count = 0
while len(heap) != 1:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    count += (x+y)
    heapq.heappush(heap,x+y)

print(count)