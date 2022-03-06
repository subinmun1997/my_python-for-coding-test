a, b = map(int, input().split())
n = int(input())
frequency = []

for _ in range(n):
    frequency.append(int(input()))

diff = []
diff.append(abs(b-a))
for f in frequency:
    diff.append(abs(f-b)+1)

print(min(diff))