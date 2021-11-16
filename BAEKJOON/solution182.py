t = int(input())

for _ in range(t):
    array = list(map(str, input().split()))
    for i in array:
        print(i[::-1], end=' ')
    print()
