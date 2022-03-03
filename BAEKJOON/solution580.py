n = int(input())

candidate = []
for _ in range(n):
    candidate.append(int(input()))

count = 0
if n == 1:
    print(0)
else:
    while True:
        if candidate[0] > max(candidate[1:]):
            break
        else:
            idx = candidate[1:].index(max(candidate[1:]))
            candidate[0] += 1
            candidate[idx+1] -= 1
            count += 1
    print(count)