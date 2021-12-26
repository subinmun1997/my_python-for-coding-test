n = int(input()) # 도시의 개수
l = list(map(int, input().split())) # 도시간 거리
m = list(map(int, input().split())) # 주유비

total = 0
start = m[0]

for i in range(len(l)):
    if m[i] < start:
        start = m[i]
    total += (l[i] * start)

print(total)