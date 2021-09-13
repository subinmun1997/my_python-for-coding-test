'''
큰 수의 법칙
'''

n, m, k = map(int, input().split()) # n : 배열 원소 수, m : 더하는 횟수, k : 연속 가능한 수
data = list(map(int, input().split()))
data.sort()

result = 0
first = data[n-1]
second = data[n-2]

while True:
    if m == 0:
        break
    else:
        for i in range(k):
            result += first
            m -= 1
        result += second
        m -= 1

print(result)