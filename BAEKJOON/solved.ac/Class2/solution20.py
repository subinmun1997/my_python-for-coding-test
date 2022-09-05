t = int(input())

home = []
for _ in range(t):
    k = int(input())
    n = int(input())

    count = [i for i in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            count[j] += count[j-1]

    print(count[-1])