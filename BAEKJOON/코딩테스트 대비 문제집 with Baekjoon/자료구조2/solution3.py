import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, (-x, x))
    else:
        if heap:
            result = heapq.heappop(heap)
            print(result[1])
        else:
            print(0)
