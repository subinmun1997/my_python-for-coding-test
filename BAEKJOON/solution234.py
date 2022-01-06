import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, x)
    if x == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap))
        else:
            print(0)
