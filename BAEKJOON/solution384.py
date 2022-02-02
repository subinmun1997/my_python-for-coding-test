def check(n, m):
    number = []
    for i in range(1, n-1):
        a = i
        for j in range(i+1, n):
            b = j
            formal = (a*a + b*b + m) / (a*b)
            if formal == int(formal):
                number.append(formal)
    return number
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    count = check(n, m)
    print(len(count))