n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k # n이 k로 나누어 떨어지지 않는 경우에 k로 나누어 떨어지는 가장 가까운 수 찾기
    result += (n-target) # k로 나누어 떨어지는 수가 되기까지 1을 몇 번 뺐는지
    n = target

    if n < k:
        break

    n //= k
    result += 1

result += (n-1)
print(result)

'''
N이 100억 이상의 큰 수가 되는 경우를 가정했을 때 빠르게 동작하려면, N이 K의 배수가 되도록 효율적으로
한 번에 빼는 방식으로 소스코드를 작성할 수 있다.
'''