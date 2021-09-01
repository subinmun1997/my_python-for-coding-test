n = int(input())
k = list(map(int, input().split()))

d = [0] * 100 # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = k[0]
d[1] = max(k[0],k[1])
for i in range(2, n):
    d[i] = max(d[i-1],d[i-2]+k[i])

print(d[n-1])
