import heapq

n = int(input())
hw = [list(map(int, input().split())) for _ in range(n)]
hw.sort(key=lambda x : x[0])

p_list = []
for i in hw:
    heapq.heappush(p_list, i[1])
    if len(p_list) > i[0]:
        heapq.heappop(p_list)

print(sum(p_list))

