n = int(input())

for _ in range(n):
    p = int(input())
    array = []
    for _ in range(p):
        a, b = map(str, input().split())
        array.append((int(a), b))

    array.sort(reverse=True)
    print(array[0][1])