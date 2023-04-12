import math

# 시험장의 개수
n = int(input())
# 각 시험장에 있는 응시자 수
candidate = list(map(int, input().split()))
# b=총감독관, c=부감독관
b, c = map(int, input().split())

# 필요한 감독관의 최소 수
result = 0
for cand in candidate:
    # 총감독관 혼자 감독이 가능한 상황이라면
    if cand <= b:
        result += 1
    # 부감독관도 필요한 상황이라면
    else:
        result += math.ceil((cand-b) / c) + 1

print(result)