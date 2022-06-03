import heapq, sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    heap = []
    answer = 0
    for i in num:
        heapq.heappush(heap, i)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        answer += (a+b)
        heapq.heappush(heap, a+b)

    print(answer)
