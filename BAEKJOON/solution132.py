n = int(input())
graph = []

for i in range(n):
    a, b = map(int, input().split())
    graph.append((a,b))

graph = sorted(graph, key=lambda x:(x[0],x[1]))

for x,y in graph:
    print(x,y)