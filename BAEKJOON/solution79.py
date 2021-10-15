def two(num):
    if (num == 1):
        return False
    for i in range(2, int((num ** 0.5) + 1)):
        if (num % i == 0):
            return False
    return True


lst = list(range(2, 246912))
ans = []
for i in lst:
    if two(i):
        ans.append(i)

while True:
    answer = 0
    n = int(input())
    if (n == 0):
        break
    for i in ans:
        if (n < i<=n * 2):
            answer += 1

    print(answer)