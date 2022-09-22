n, m = map(int, input().split())
listen = set(input() for _ in range(n))
see = set(input() for _ in range(m))

count = 0
answer = []
for i in listen:
    if i in see:
        count += 1
        answer.append(i)

print(count)

answer.sort()
for i in answer:
    print(i)