'''
문제 : 볼링공 고르기

문제 해설 : 이 문제를 해결하기 위해서는, 먼저 무게마다 볼링공이 몇 개 있는지를 계산해야 한다.
            A가 특정한 무게의 볼링공을 선택했을 때, 이어서 B가 볼링공을 선택하는 경우를 차례대로 계산하여
            문제를 해결할 수 있다.
'''

n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11 # 1부터 10까지의 무게를 담을 수 있는 리스트
for x in data:
    array[x] += 1 # 각 무게에 해당하는 볼링공의 개수 카운트

result = 0
for i in range(1, m+1): # 1부터 m까지의 각 무게에 대하여 처리
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i]*n # B가 선택하는 경우의 수와 곱하기

print(result)