def turn45(n, d, graph):
    count = abs(d) // 45
    minus = False
    if d < 0:
        minus = True

    for _ in range(count):
        if not minus:
            prev_list = []

            for i in range(n): #주 대각선
                prev_list.append(graph[i][i])

            for i in range(n): #주 대각선 > 가운데열
                prev_temp = graph[i][n//2]
                graph[i][n//2] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n): #가운데열 > 부 대각선
                prev_temp = graph[i][n-1-i]
                graph[i][n-1-i] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n): #부 대각선 > 가운데행
                prev_temp = graph[n//2][n-1-i]
                graph[n//2][n-1-i] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n): #가운데 행 > 주대각선
                graph[n-1-i][n-1-i] = prev_list[i]
        else:
            prev_list = []

            for i in range(n): #주 대각선
                prev_list.append(graph[i][i])

            for i in range(n): #주 대각선 > 가운데 행
                prev_temp = graph[n//2][i]
                graph[n//2][i] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n): #가운데 행 > 부 대각선
                prev_temp = graph[n-1-i][i]
                graph[n-1-i][i] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n): #부 대각선 > 가운데 열
                prev_temp = graph[n-1-i][n//2]
                graph[n-1-i][n//2] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n): #가운데 열 > 주 대각선
                graph[n-1-i][n-1-i] = prev_list[i]

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    turn45(n, d, graph)

    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=' ')
        print()