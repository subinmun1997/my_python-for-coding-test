import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
'''
[abs(x),x] 의 형태로 삽입을 하게 되면 문제에서 요구하는 절댓값은 같더라도, 값 자체가 작은 수 순서로 정렬이 되게 됩니다.
'''
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            result = heapq.heappop(heap)
            print(result[1])
        else:
            print(0)