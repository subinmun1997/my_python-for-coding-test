n = int(input())
ans = 0
for i in range(n):
    a = '0'
    check = []
    s = input()
    for j in s:
        if j != a:
            check.append(j)
        a = j
    if len(check) == len(set(check)):
        ans += 1
print(ans)