import math

n = int(input()) # 시험장 수
a = list(map(int, input().split())) # 각 시험장마다 응시자 수
b, c = map(int, input().split()) # 총감독관, 부감독관이 각각 감시할 수 있는 인원 수

result = 0
for i in a:
    # i <= b일 경우가 존재하기 때문에 해당 조건문을 꼭 걸어줘야함
    if i <= b: # 만약 해당 시험장의 모든 응시자를 총감독관이 감시 가능하다면
        result += 1 # 총 감독관만 있으면 됨
    else: # 아니라면
        result += (math.ceil((i - b) / c) + 1) # 총 감독관(1명) + 부감독관

print(result)