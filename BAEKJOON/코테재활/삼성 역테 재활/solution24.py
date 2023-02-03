from collections import Counter

def rc():
    max_len = 0
    graph_len = len(graph)
    for i in range(graph_len):
        temp = [k for k in graph[i] if k != 0]
        temp = Counter(temp).most_common()
        temp.sort(key=lambda x : (x[1], x[0]))
        graph[i] = []

        for x, y in temp:
            graph[i].append(x)
            graph[i].append(y)
        temp_len = len(temp)

        if max_len < temp_len * 2:
            max_len = temp_len * 2

    for j in range(graph_len):
        for k in range(max_len - len(graph[j])):
            graph[j].append(0)
        graph[j] = graph[j][:100]

r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]

for i in range(101):
    try:
        if graph[r-1][c-1] == k:
            print(i)
            break
    except: pass

    if len(graph) < len(graph[0]): # C연산
        # zip함수를 이용한 전치행렬
        graph = list(zip(*graph))
        rc()
        graph = list(zip(*graph))
    else: # R연산
        rc()
else:
    print(-1)