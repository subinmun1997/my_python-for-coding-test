n = int(input())

t_list = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            t_list[i][j] += t_list[i-1][j]
        elif j == i:
            t_list[i][j] += t_list[i-1][j-1]
        else:
            t_list[i][j] = max(t_list[i][j] + t_list[i-1][j], t_list[i][j] + t_list[i-1][j-1])

print(max(t_list[n-1]))