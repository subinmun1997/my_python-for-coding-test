n = int(input())
file = {}

for _ in range(n):
    file_name = input().split('.')
    if file_name[1] in file:
        file[file_name[1]] += 1
    else:
        file[file_name[1]] = 1

result = sorted(file.items())
for i in result:
    print(*i)
