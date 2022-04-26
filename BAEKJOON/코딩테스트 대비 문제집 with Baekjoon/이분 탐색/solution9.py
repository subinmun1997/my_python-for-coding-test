import sys
from bisect import bisect_left

input = sys.stdin.readline
n, m = map(int, input().split())

nameList = []
powerList = []
for _ in range(n):
    name, power = input().split()
    power = int(power)
    if powerList and powerList[-1] == power:
        continue
    nameList.append(name)
    powerList.append(power)

for _ in range(m):
    p = int(input())
    idx = bisect_left(powerList, p)
    print(nameList[idx])