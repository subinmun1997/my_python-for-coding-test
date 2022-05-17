import heapq

def solution(scoville, k):
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)

    cnt = 0
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        cnt += 1

    return cnt

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2], 7))
print(solution([6], 7))