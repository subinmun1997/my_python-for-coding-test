n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k # n이 k로 나누어 떨어지지 않는 경우에 k로 나누어 떨어지는 가장 가까운 수를 찾고자 할 때
    result += (n-target) # k로 나누어 떨어지는 수가 되기까지의 1을 몇번 뺏는지
    n = target

    if n < k:
        break
    n //= k
    result += 1

result += (n-1)
print(result)