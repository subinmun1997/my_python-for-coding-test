n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
room.sort(key=lambda x : (x[1]. x[0]))

result = 0
prevs = prevf = 0
for s, f in room:
    if prevf <= s:
        result += 1
        prevf = f

print(result)
