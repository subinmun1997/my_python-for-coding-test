import heapq
import sys

input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(heap,(-x,x))
    elif x == 0:
        if len(heap) != 0:
            k = heapq.heappop(heap)[1]
            print(k)
        else:
            print(0)