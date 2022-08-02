n, m = map(int, input().split())
number = list(map(int, input().split()))
count = 0

if n == 1:
    print(1 if number[0] == m else 0)
else:
    first = 0
    second = 1
    while second <= n-1:
        temp = sum(number[first:second+1])
        if temp < m:
            second += 1
        elif temp > m:
            first += 1
        else:
            count += 1
            first += 1
            second += 1

    print(count)
