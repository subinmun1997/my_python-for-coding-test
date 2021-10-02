n = int(input())
data = list(map(int, input().split()))

for i in data:
    if i == 1:
        n -= 1
        continue

    # 에라토스테네스의 체
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            n -= 1
            break

print(n)