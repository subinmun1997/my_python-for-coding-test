n = int(input())
score = list(map(int, input().split()))
m = max(score)

new_score = []
for s in score:
    new_score.append(s/m*100)

print(sum(new_score)/len(new_score))
