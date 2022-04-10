n, m = map(int, input().split())
a = set(input() for _ in range(n))
b = set(input() for _ in range(m))

result = []
for i in a:
    if i in b:
        result.append(i)

result.sort()
print(len(result))
for i in result:
    print(i)