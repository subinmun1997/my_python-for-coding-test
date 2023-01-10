import heapq, sys
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
