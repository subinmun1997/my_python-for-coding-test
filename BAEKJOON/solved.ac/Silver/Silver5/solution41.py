score = [int(input()) for _ in range(8)]
sortedScore = sorted(score, reverse=True)
idx = []

for i in range(5):
    idx.append(score.index(sortedScore[i])+1)

print(sum(sortedScore[:5]))
print(*sorted(idx))
