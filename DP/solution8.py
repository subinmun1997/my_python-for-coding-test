'''
적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾으면 된다.
금액 i를 만들 수 있는 최소한의 화폐 개수를 a(i), 화폐의 단위를 k라고 했을 때 다음과 같이 점화식을 작성할 수 있다.
a(i-k)는 금액 (i-k)를 만들 수 있는 최소한의 화폐 개수를 의미한다.

a(i-k)를 만드는 방법이 존재하는 경우, a(i) = min(a(i), a(i-k)+1)
a(i-k)를 만드는 방법이 존재하지 않는 경우 a(i) = 10,001
'''

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