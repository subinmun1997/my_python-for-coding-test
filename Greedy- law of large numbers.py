n,m,k = map(int,input().split()) # n = 배열의 크기 m = 숫자가 더해지는 횟수 k = 연속해서 몇번까지?
data = list(map(int,input().split()))

data.sort()
first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수

result = 0

while True:
    for i in range(k): #최대 k번까지 더할 수 있음
        if m == 0: # 숫자가 더해지는 횟수가 0 이라면
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second # 두 번째로 큰 수 한 번 더함
    m -= 1

print(result)
