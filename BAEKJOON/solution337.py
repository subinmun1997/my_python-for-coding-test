t = int(input())

for _ in range(t):
    car = int(input())
    n = int(input())

    options = 0
    for _ in range(n):
        x, y = map(int, input().split())
        options += x * y

    print(car+options)
