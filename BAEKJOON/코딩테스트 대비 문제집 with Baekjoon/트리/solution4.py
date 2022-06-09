k = int(input())
enter = list(map(int, input().split()))
answer = [[] for _ in range(k)]

def makeTree(arr, depth):
    mid = len(arr) // 2
    answer[depth].append(arr[mid])
    if len(arr) == 1:
        return
    makeTree(arr[:mid], depth+1)
    makeTree(arr[mid+1:], depth+1)

makeTree(enter, 0)
for i in range(k):
    print(*answer[i])