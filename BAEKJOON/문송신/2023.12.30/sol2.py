n, m = map(int, input().split())

friends = [0 for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a-1] += 1
    friends[b-1] += 1

for f in friends:
    print(f)