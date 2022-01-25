n = int(input())

apple = 0
for _ in range(n):
    a, b = map(int, input().split())
    apple += (b%a)

print(apple)