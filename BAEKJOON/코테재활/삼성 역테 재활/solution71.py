from copy import deepcopy

def move(graph, dir):
    if dir == 0: # 오른쪽으로 이동하기
        for i in range(n):
            # 오른쪽으로 이동할 때 기준이 되는 위치
            top = n-1
            for j in range(n-2, -1, -1):
                # 해당 위치에 값이 있으면
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    # 기준이 되는 위치의 값과 옮기려는 값이 동일하다면
                    if graph[i][top] == temp:
                        graph[i][top] *= 2
                        # 옮겼으면 기준 위치 하나 왼쪽으로 앞당기기
                        top -= 1
                    # 기준이 되는 위치에 값이 없다면, 옮기려는 값을 그 자리에 저장
                    elif graph[i][top] == 0:
                        graph[i][top] = temp
                    # 기준이 되는 위치의 값과 옮기려는 값이 동일하지 않다면
                    # 기준 위치 하나 왼쪽으로 앞당기고 그 자리에 값 저장
                    else:
                        top -= 1
                        graph[i][top] = temp

    elif dir == 1: # 왼쪽으로 이동하기
        for i in range(n):
            # 왼쪽으로 이동할 때 기준이 되는 위치
            top = 0
            for j in range(1, n):
                # 해당 위치에 값이 있다면
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    # 기준이 되는 위치의 값과 옮기려는 값이 동일하다면
                    if graph[i][top] == temp:
                        graph[i][top] *= 2
                        # 옮겼으면 기준 위치 하나 오른쪽으로 밀기
                        top += 1
                    # 기준이 되는 위치에 값이 없다면, 옮기려는 값을 그 자리에 저장
                    elif graph[i][top] == 0:
                        graph[i][top] = temp
                    # 기준이 되는 위치의 값과 옮기려는 값이 동일하지 않다면
                    # 기준 위치 하나 오른쪽으로 밀고 그 자리에 값 저장
                    else:
                        top += 1
                        graph[i][top] = temp

    elif dir == 2: # 아래쪽으로 이동하기
        for j in range(n):
            # 아래쪽으로 이동할 때 기준이 되는 위치
            top = n-1
            for i in range(n-2, -1, -1):
                # 해당 위치에 값이 있다면
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    # 기준이 되는 위치의 값과 옮기려는 값이 동일하다면
                    if graph[top][j] == temp:
                        graph[top][j] *= 2
                        # 옮겼으면 기준 위치 하나 위로 올려주기
                        top -= 1
                    # 기준이 되는 위치에 값이 없다면, 옮기려는 값을 그 자리에 저장
                    elif graph[top][j] == 0:
                        graph[top][j] = temp
                    # 기준이 되는 위치의 값과 옮기려는 값이 동일하지 않다면
                    # 기준 위치 하나 위쪽으로 올리고 그 자리에 값 저장
                    else:
                        top -= 1
                        graph[top][j] = temp

    elif dir == 3: # 위쪽으로 이동하기
        for j in range(n):
            # 위쪽으로 이동할 때 기준이 되는 위치
            top = 0
            for i in range(1, n):
                # 해당 위치에 값이 있다면
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    # 기준이 되는 위치의 값과 옮기려는 값이 동일하다면
                    if graph[top][j] == temp:
                        graph[top][j] *= 2
                        # 옮겼으면 기준 위치 하나 아래로 내려주기
                        top += 1
                    # 기준이 되는 위치에 값이 없다면, 옮기려는 값을 그 자리에 저장
                    elif graph[top][j] == 0:
                        graph[top][j] = temp
                    # 기준이 되는 위치의 값과 옮기려는 값이 동일하지 않다면
                    # 기준 위치 하나 아래로 내리고 그 자리에 값 저장
                    else:
                        top += 1
                        graph[top][j] = temp

    return graph

# 보드의 크기
n = int(input())
# 보드의 초기 상태
graph = [list(map(int, input().split())) for _ in range(n)]

# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값
result = 0
def dfs(graph, cnt):
    global result

    # 5번 이동했으면 가장 큰 값 구하기
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                result = max(result, graph[i][j])
        return

    # 5번 이동 안했으면, 상하좌우 이동 진행하기
    for i in range(4):
        temp_graph = move(deepcopy(graph), i)
        dfs(temp_graph, cnt + 1)

dfs(graph, 0)
print(result)