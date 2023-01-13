t = int(input())

for _ in range(t):
    n = int(input())
    clothes = dict()
    for _ in range(n):
        kind, target = map(str, input().split())
        if target not in clothes:
            clothes[target] = 1
        else:
            clothes[target] += 1

    answer = 1
    for i in clothes.values():
        answer *= (i+1)

    print(answer - 1)
