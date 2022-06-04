import heapq, sys
input = sys.stdin.readline

n = int(input())
number = [int(input()) for _ in range(n)]
heap = []
answer = 0

for num in number:
    heapq.heappush(heap, num)

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    answer += (a+b)
    heapq.heappush(heap, a+b)

print(answer)