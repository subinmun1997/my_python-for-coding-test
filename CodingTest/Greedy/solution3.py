'''
문제 : 큰 수의 법칙
문제 해설 : 이 문제를 해결하려면 일단 입력 값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.
            연속으로 더할 수 있는 횟수는 최대 k번이므로 가장 큰 수를 k번 더하고 두 번재로 큰 수를 한 번 더하는 연산을
            반복하면 된다.
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split())) # n개의 수를 공백으로 구분하여 입력받기

data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k번 더하기
        if m == 0:
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0:
        break
    result += second
    m -= 1

print(result)