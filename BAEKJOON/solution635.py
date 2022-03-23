n, c = map(int, input().split()) # 마을 수, 트럭 용량
m = int(input()) # 박스 개수

truck = [list(map(int, input().split())) for _ in range(m)]
truck.sort(key=lambda x : x[1])

box = [c] * (n+1)
answer = 0
for s, e, b in truck:
    _min = c
    for i in range(s, e):
        _min = min(_min, box[i])
    _min = min(_min, b)
    for i in range(s, e):
        box[i] -= _min

    answer += _min

print(answer)
