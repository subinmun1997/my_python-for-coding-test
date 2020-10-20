n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<= -1 or x>= n or y<= -1 or y>= m: #주어진 범위를 벗어나는 경우에는 즉시 종료
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y) #상  #상하좌우 모두 재귀적으로 호출
        dfs(x, y-1)# 좌
        dfs(x+1,y) #하
        dfs(x,y+1) #우
        return True
    return False

result = 0
for i in range(n): # 모든 노드에 대하여 음료수 채우기
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)
