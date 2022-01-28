def divisor(n):
    count = []
    for i in range(1, n+1):
        if n%i == 0:
            count.append(i)
    return count

n, k = map(int, input().split())
result = divisor(n)
result.sort()
if len(result) < k:
    print(0)
else:
    print(result[k-1])