n,m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1) # 0원부터 m원까지 최소한의 화폐개수 크기의 table 생성

d[0] = 0 # 0원은 그냥 생성 가능하니까 0으로 초기화
for i in range(n): # i = 각각의 화폐 단위
    for j in range(array[i], m+1): # j = 금액의 단위. 현재 금액부터 m원까지
        if d[j-array[i]] != 10001: # 현재 금액에서 확인하고 있는 화폐의 단위를 뺀 그 금액을 만들 수 있다면
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])