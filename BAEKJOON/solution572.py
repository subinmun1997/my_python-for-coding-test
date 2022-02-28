n, m = map(int, input().split())
array = [i for i in range(1, n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    array[x-1], array[y-1] = array[y-1], array[x-1]

print(*array)