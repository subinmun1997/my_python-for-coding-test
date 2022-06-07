n, k = map(int, input().split())
a = list(map(int, input().split()))
l, r = 0, 0

cnt = [0] * (max(a) + 1)
answer = 0
while r < n:
    if cnt[a[r]] < k:
        cnt[a[r]] += 1
        r += 1
    else:
        cnt[a[l]] -= 1
        l += 1
    answer = max(answer, r-l)
print(answer)