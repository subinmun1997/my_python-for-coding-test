def check(word):
    vowel = 'aeiou'
    v_cnt = 0

    for w in word:
        if w in vowel:
            v_cnt += 1

    if v_cnt >= 1 and len(word) - v_cnt >= 2:
        print("".join(word))

temp = []
def dfs(cnt, start):
    if cnt == l:
        check(temp)
        return

    for i in range(start, c):
        if not visited[i]:
            visited[i] = True
            temp.append(alpha[i])
            dfs(cnt+1, i+1)
            visited[i] = False
            temp.pop()

l, c = map(int, input().split())
alpha = sorted(list(map(str, input().split())))
visited = [False] * c

dfs(0, 0)
