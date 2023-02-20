n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

s = []
def dfs(start):
    if len(s) == m:
        print(*s)
        return
    for i in range(start, n):
        s.append(nums[i])
        dfs(i)
        s.pop()

dfs(0)