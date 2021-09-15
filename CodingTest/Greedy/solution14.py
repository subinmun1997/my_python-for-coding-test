'''
문제 : 만들 수 없는 금액

문제 해설 : 이 문제는 정렬을 이용한 그리디 알고리즘으로 해결할 수 있는 문제이다.
            동전에 대한 정보가 주어졌을 때, 화폐 단위를 기준으로 오름차순 정렬한다. 이후에 1부터 차례대로 특정한 금액을
            만들 수 있는지 확인하면 된다. 만약 만들 수 있다면 target 값을 업데이트하는 방식을 이용한다
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for i in data:
    if target < i:
        break
    target += i

print(target)