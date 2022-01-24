from itertools import combinations
import sys

input = sys.stdin.readline
while True:
    data = list(map(str, input().split()))
    if data[0] == 0 and len(data) == 1:
        break

    length = data.pop(0)

    for comb in combinations(data, 6):
        temp = list(map(str, comb))
        print(" ".join(temp))
    print()
