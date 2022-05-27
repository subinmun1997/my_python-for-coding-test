n, k = map(int, input().split())
course = list(map(int, input().split()))

for i in range(n):
    k -= course[i]
    if k < 0:
        print(i+1)
        break
else:
    for i in range(n-1, -1, -1):
        k -= course[i]
        if k < 0:
            print(i+1)
            break