import sys
input = sys.stdin.readline

n = int(input())
dict = {}

for _ in range(n):
    a = int(input())
    if a not in dict:
        dict[a] = 1
    else:
        dict[a] += 1

sort_dict = sorted(dict.items(), key=lambda x : (-x[1],x[0]))

print(sort_dict[0][0])