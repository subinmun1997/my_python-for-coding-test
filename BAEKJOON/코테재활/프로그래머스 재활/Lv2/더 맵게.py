from heapq import *

def solution(scoville, k):
    count = 0
    heapify(scoville)
    while scoville[0] < k and len(scoville) > 1:
        heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        count += 1

    return count if scoville[0] >= k else -1

print(solution([1,2,3,9,10,12], 7))
print(solution([10,8,5,3,2,4,1],6))