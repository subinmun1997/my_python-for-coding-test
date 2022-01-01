import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewel = []
bag = []
for _ in range(N):
    heapq.heappush(jewel, list(map(int, input().split())))
for _ in range(K):
    bag.append(int(input()))

bag.sort()

result = 0
candidate = []
for b in bag:
    while jewel and b >= jewel[0][0]:
        w, v = heapq.heappop(jewel)
        heapq.heappush(candidate, -v)

    if candidate:
        result -= heapq.heappop(candidate)


print(result)