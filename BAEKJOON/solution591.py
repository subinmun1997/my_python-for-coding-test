n, m, k = map(int, input().split())

candidate = {}
for i in range(n):
    candidate[i+1] = 0

for i in range(m):
    genre = list(map(float, input().split()))
    for j in range(0, 2*n, 2):
        if genre[j+1] > candidate[genre[j]]:
            candidate[genre[j]] = genre[j+1]

score = sorted(list(candidate.values()), reverse=True)
result = sum(score[:k])
print(f"{result:.1f}")
