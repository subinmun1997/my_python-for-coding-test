import sys
import heapq
input = sys.stdin.readline

n = int(input())

leftHeap = []
rightHeap = []
answer = []

for i in range(n):

    num = int(input())
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, (-num, num))
    else:
        heapq.heappush(rightHeap, (num, num))

    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        min = heapq.heappop(rightHeap)[0]
        max = heapq.heappop(leftHeap)[1]
        heapq.heappush(leftHeap, (-min, min))
        heapq.heappush(rightHeap, (max, max))

    answer.append(leftHeap[0][1])

for j in answer:
    print(j)