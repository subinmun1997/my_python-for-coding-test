import sys
input = sys.stdin.readline

n = int(input())
dict = {}
for _ in range(n):
    book = input().rstrip()
    if book not in dict:
        dict[book] = 1
    else:
        dict[book] += 1

d = sorted(dict.items(), key=lambda x : (-x[1],x[0]))

print(d[0][0])