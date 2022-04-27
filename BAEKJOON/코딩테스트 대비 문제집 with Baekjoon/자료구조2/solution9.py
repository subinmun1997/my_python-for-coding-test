import sys, heapq

input = sys.stdin.readline

minHeap = []
maxHeap = []
key = dict()

n = int(input())
for _ in range(n):
    p, level = map(int, input().split())
    heapq.heappush(minHeap, (level, p))
    heapq.heappush(maxHeap, (-level, -p))
    key[p] = False

m = int(input())
for _ in range(m):
    order = input().split()
    if order[0] == "recommend":
        if order[1] == "1":
            print(-maxHeap[0][1])
        elif order[1] == "-1":
            print(minHeap[0][1])
    elif order[0] == "add":
        heapq.heappush(minHeap, (int(order[2]), int(order[1])))
        heapq.heappush(maxHeap, (-int(order[2]), -int(order[1])))
        key[int(order[1])] = False
    elif order[0] == "solved":
        key[int(order[1])] = True
        while key[-maxHeap[0][1]]:
            print(heapq.heappop(maxHeap))
        while key[minHeap[0][1]]:
            print(heapq.heappop(minHeap))

