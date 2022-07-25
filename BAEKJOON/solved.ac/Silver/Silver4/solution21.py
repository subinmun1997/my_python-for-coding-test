n = int(input())
rope = sorted([int(input()) for _ in range(n)], reverse=True)

max_weight = []
for i in range(n):
    max_weight.append(rope[i] * (i+1))

print(max(max_weight))