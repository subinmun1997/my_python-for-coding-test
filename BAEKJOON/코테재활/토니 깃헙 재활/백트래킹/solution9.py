n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []

def dfs():
    if len(s) == m:
        print(*s)
        return
    for i in nums:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()