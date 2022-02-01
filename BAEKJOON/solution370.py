t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    array = [str(i) for i in range(n, m+1)]
    count = 0
    for a in array:
        count += a.count('0')
    print(count)