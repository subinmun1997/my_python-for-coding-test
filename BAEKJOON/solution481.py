n = int(input())

for i in range(1, n+1):
    n, d, a, b, f = map(float, input().split())
    mile = (d / (a+b)) * f
    print(f"{i} {mile:.6f}")