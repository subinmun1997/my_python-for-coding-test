def solution():
    n, k = map(int, input().split())
    min_value = k*(k+1)//2
    if min_value > n:
        return -1
    if (n-min_value) % k == 0:
        return k-1
    else:
        return k

print(solution())
