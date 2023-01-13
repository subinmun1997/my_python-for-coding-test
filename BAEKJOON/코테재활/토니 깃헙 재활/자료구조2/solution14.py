import heapq, sys
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    num = int(input())
    if num:
        heapq.heappush(heap, num)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)