import heapq
n = int(input())
cards = [int(input()) for _ in range(n)]
result = 0

heap = []
for card in cards:
    heapq.heappush(heap, card)

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    result += (a+b)
    heapq.heappush(heap, (a+b))

print(result)

