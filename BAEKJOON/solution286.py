scores = []

for i in range(5):
    x = list(map(int, input().split()))
    scores.append(sum(x))

max_score = max(scores)
print(scores.index(max_score)+1, end=' ')
print(max_score)