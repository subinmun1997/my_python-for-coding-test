a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

cost = min(p * a, (b if p <= c else b + (p-c) * d))

print(cost)