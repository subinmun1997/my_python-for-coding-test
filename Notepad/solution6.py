n, k = map(int, input().split())
answer = 0

while True:
    target = (n//k) * k
    answer += (n - target)
    n = target

    if n < k:
        break
    n //= k
    answer += 1

answer += (n-1)
print(answer)