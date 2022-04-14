import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()

for _ in range(n):
    s.add(input().rstrip())

result = 0
for _ in range(m):
    check = input().rstrip()
    if check in s:
        result += 1

print(result)

