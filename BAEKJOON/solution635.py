n, c = map(int, input().split()) # 마을 수, 트럭 용량
m = int(input()) # 박스 개수

truck = [list(map(int, input().split())) for _ in range(m)]
truck.sort(key=lambda x : x[1])

box = [c] * (n+1)
answer = 0

for s, r, b in truck:
    min_box = min(min(truck[s:r]), b)
    for i in range(s, r):
        box[i] -= min_box
    answer += min_box

print(answer)
