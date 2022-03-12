n = int(input())

file_dict = {}
for _ in range(n):
    file = input()
    x = file.split(".")
    if x[1] in file_dict:
        file_dict[x[1]] += 1
    else:
        file_dict[x[1]] = 1

file_dict = sorted(file_dict.items())
for file in file_dict:
    print(*file)
