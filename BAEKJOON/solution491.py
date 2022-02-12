a = list(map(int, input().split())) #제미니스
b = list(map(int, input().split())) #걸리버스

check = False # 역전패인지 아닌지 체크

score_a = 0
score_b = 0

for i in range(len(a)):
    score_a += a[i]
    if score_a > score_b:
        check = True
    score_b += b[i]

print("Yes" if score_a < score_b and check else "No")