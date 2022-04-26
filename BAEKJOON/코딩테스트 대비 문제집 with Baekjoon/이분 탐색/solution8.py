import sys
input = sys.stdin.readline

n, m = map(int, input().split())
powerList = []
nameList = []
for _ in range(n):
    name, power = input().split()
    power = int(power)
    if powerList and powerList[-1] == power:
        continue
    powerList.append(power)
    nameList.append(name)

def check_power(p):
    left = 0
    right = len(powerList) - 1

    while left <= right:
        mid = (left + right) // 2
        if p > powerList[mid]:
            left = mid + 1
        else:
            right = mid - 1

    print(nameList[right+1])

for _ in range(m):
    p = int(input())
    check_power(p)