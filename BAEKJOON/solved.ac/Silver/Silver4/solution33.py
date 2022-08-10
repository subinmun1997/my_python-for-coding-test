import math

n = int(input())
ring = list(map(int, input().split()))

div = ring[0]
for i in range(1, n):
    gcd = math.gcd(div, ring[i])
    print(f"{div//gcd}/{ring[i]//gcd}")