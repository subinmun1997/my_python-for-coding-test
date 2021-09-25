n = int(input())
data = [input() for _ in range(n)]

for d in data:
    score = 0
    count = 0
    for i in d: # OOXXOOXXOO
        if i == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)


