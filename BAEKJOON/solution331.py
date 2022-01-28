t = int(input())

for _ in range(t):
    n = int(input())
    array = []
    for _ in range(n):
        x, y = map(str, input().split())
        array.append((x, int(y)))
    array.sort(reverse=True, key=lambda x : x[1])
    print(array[0][0])
