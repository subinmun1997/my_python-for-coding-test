n, m = map(int, input().split())
arr1 = set(input() for _ in range(n))
arr2 = set(input() for _ in range(m))

result = sorted([i for i in arr1 if i in arr2])

print(len(result))
for i in result:
    print(i)