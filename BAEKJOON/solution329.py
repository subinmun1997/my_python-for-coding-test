n = int(input())

chang = sang = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        continue
    elif a > b:
        sang -= a
    else:
        chang -= b

print(chang)
print(sang)