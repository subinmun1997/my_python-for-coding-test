scores = []
for _ in range(8):
    scores.append(int(input()))

result = sorted(scores, reverse=True)
result = result[:5]
print(sum(result))

idx = []
for i in range(len(scores)):
    if scores[i] in result:
        idx.append(i+1)

idx.sort()
for i in idx:
    print(i, end=' ')