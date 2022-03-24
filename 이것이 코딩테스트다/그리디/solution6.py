n, k = map(int, input().split())
answer = 0

while True:
    target = (n//k) * k # n이 k로 나누어 떨어지지 않는 경우에 k로 나누어 떨어지는 가장 가까운 수
    answer += (n-target) # k로 나누어 떨어지는 수가 되기까지 1을 몇 번 뺐는지
    n = target

    if n < k:
        break
    n //= k
    answer += 1

answer += (n-1) # 남은 수에 대해서 1씩 빼기
print(answer)