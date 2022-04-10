n = int(input())
file_dict = {}

for _ in range(n):
    data = input().split('.')
    if data[1] in file_dict:
        file_dict[data[1]] += 1
    else:
        file_dict[data[1]] = 1

result = sorted(list(file_dict.items()))
for i in result:
    print(*i)