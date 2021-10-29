n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0

for i in range(n):
    result += max(b) * min(a)
    b.pop(b.index(max(b)))
    a.pop(a.index(min(a)))

print(result)