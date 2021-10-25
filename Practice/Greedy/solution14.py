n = int(input())
coin = list(map(int, input().split()))
coin.sort()

result = 1
for i in coin:
    if result < i:
        break
    result += i

print(result)

'''
아이디어 : 동전에 대한 정보가 주어졌을 때, 화폐 단위를 기준으로 오름차순 정렬한다.
           1부터 result - 1까지의 모든 금액을 만들 수 있다고 가정하고, 화폐 단위가
           작은 순서대로 동전을 확인하며, 현재 확인하는 동전을 이용해 result 금액 또한
           만들 수 있는지 확인하면 된다. 만약 result 금액을 만들 수 있다면, result 값을
           업데이트하는 방식을 이용한다.
'''

