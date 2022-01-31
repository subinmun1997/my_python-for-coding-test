k = int(input())

for _ in range(k):
    p, m = map(int, input().split())
    array = set()
    for _ in range(p):
        array.add(int(input()))

    print(p - len(array))