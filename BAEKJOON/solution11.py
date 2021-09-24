import sys
n = int(sys.stdin.readline())

data = [int(sys.stdin.readline()) for _ in range(n)]
data.sort()

for i in data:
    print(i)