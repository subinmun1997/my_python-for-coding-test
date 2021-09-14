'''
문제에서는 n의 범위가 10만 이하이므로, 이처럼 일일이 1씩 빼도 문제를 해결할 수 있다.
하지만 n이 100억 이상의 큰 수가 되는 경우를 가정했을 때에도 빠르게 동작하려면, n이 k의 배수가 되도록
효율적으로 한 번에 빼는 방식으로 소스코드를 작성할 수 있다.
'''

n, k = map(int, input().split())
result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n//k) * k # n이 k로 나누어 떨어지지 않는 경우에 k로 나누어 떨어지는 가장 가까운 수를 찾고자 할 때
    result += (n-target) # k로 나누어 떨어지는 수가 되기까지의 1을 몇번 뺐는지
    n = target

    if n < k: # n이 k보다 작아 더 이상 나눌 수 없을 때 반복문 탈출
        break
    n //= k
    result += 1

result += (n-1)
print(result)