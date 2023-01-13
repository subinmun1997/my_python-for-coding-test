n = int(input())
maratoner = dict()

for _ in range(n):
    name = input()
    if name in maratoner:
        maratoner[name] += 1
    else:
        maratoner[name] = 1

for _ in range(n-1):
    name = input()
    maratoner[name] -= 1

result = sorted(maratoner.items(), key=lambda x : x[1], reverse=True)
print(result[0][0])