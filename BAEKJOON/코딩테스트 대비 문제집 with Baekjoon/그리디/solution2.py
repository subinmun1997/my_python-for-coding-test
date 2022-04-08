n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)

result = []
for i in range(n):
    result.append(rope[i] * (i+1))

print(max(result))