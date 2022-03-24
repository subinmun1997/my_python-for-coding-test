n, k = map(int, input().split())

answer = 0
while n != 1:
    if n%k == 0: # n이 k로 나누어 떨어진다면
        n //= k
        answer += 1
    else:
        n -= 1
        answer += 1

print(answer)