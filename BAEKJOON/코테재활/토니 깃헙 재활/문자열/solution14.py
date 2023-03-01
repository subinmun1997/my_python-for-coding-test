n = int(input())

extension = dict()
for _ in range(n):
    name, ext = input().split('.')
    if ext in extension:
        extension[ext] += 1
    else:
        extension[ext] = 1

result = sorted(extension.items(), key=lambda x:x[0])
for x, y in result:
    print(x, y)