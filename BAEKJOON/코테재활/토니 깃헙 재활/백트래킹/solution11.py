n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

s = []
def dfs(start):
    if len(s) == m:
        print(*s)
        return
    for i in range(start, n):
        if nums[i] not in s:
            s.append(nums[i])
            dfs(i+1)
            s.pop()

dfs(0)